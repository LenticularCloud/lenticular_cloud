
from urllib.parse import urlencode, parse_qs

import flask
from flask import Blueprint, redirect
from flask import current_app, session
from flask import jsonify, send_file
from flask.helpers import make_response
from flask.templating import render_template
from oic.oic.message import TokenErrorResponse, UserInfoErrorResponse, EndSessionRequest

from pyop.access_token import AccessToken, BearerTokenError
from pyop.exceptions import InvalidAuthenticationRequest, InvalidAccessToken, InvalidClientAuthentication, OAuthError, \
    InvalidSubjectIdentifier, InvalidClientRegistrationRequest
from pyop.util import should_fragment_encode

from flask import Blueprint, render_template, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import redirect
import logging
from datetime import timedelta
import pyotp
from base64 import b64decode, b64encode
from flask_dance.consumer import oauth_authorized
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.consumer import OAuth2ConsumerBlueprint

from ..model import User, SecurityUser, Totp
from ..model_db import OAuth, db, User as DbUser
from ..form.login import LoginForm
from ..form.frontend import ClientCertForm, TOTPForm, TOTPDeleteForm
from ..auth_providers import AUTH_PROVIDER_LIST


frontend_views = Blueprint('frontend', __name__, url_prefix='')


def init_login_manager(app):
    @app.login_manager.user_loader
    def user_loader(username):
        return User.query().by_username(username)

    @app.login_manager.request_loader
    def request_loader(request):
        pass

    @app.login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('oauth.login'))

    base_url = app.config['HYDRA_PUBLIC_URL']
    example_blueprint = OAuth2ConsumerBlueprint(
        "oauth", __name__,
        client_id=app.config['OAUTH_ID'],
        client_secret=app.config['OAUTH_SECRET'],
        base_url=base_url,
        token_url=f"{base_url}/oauth2/token",
        authorization_url=f"{base_url}/oauth2/auth",
        scope=['openid', 'profile', 'manage']
    )
    app.register_blueprint(example_blueprint, url_prefix="/")
    app.oauth = example_blueprint

    @oauth_authorized.connect_via(app.oauth)
    def github_logged_in(blueprint, token):
        if not token:
            flash("Failed to log in.", category="error")
            return False
        print(f'debug ---------------{token}')

        resp = blueprint.session.get("/userinfo")
        if not resp.ok:
            msg = "Failed to fetch user info from GitHub."
            flash(msg, category="error")
            return False

        oauth_info = resp.json()

        db_user = DbUser.query.get(str(oauth_info["sub"]))
        oauth_username = db_user.username

        # Find this OAuth token in the database, or create it
        query = OAuth.query.filter_by(
            provider=blueprint.name,
            provider_username=oauth_username,
        )
        try:
            oauth = query.one()
        except NoResultFound:
            oauth = OAuth(
                provider=blueprint.name,
                provider_username=oauth_username,
                token=token,
            )


        login_user(SecurityUser(oauth.provider_username))
        #flash("Successfully signed in with GitHub.")

        # Since we're manually creating the OAuth model in the database,
        # we should return False so that Flask-Dance knows that
        # it doesn't have to do it. If we don't return False, the OAuth token
        # could be saved twice, or Flask-Dance could throw an error when
        # trying to incorrectly save it for us.
        return True

    @frontend_views.route('/logout')
    def logout():
        logout_user()
        return redirect(f'{current_app.config["HYDRA_PUBLIC_URL"]}/oauth2/sessions/logout')


@frontend_views.route('/', methods=['GET'])
@login_required
def index():
    return render_template('frontend/index.html.j2')


@frontend_views.route('/client_cert')
@login_required
def client_cert():
    client_certs = {}
    for service in current_app.lenticular_services.values():
        client_certs[str(service.name)] = current_app.pki.get_client_certs(current_user, service)

    return render_template('frontend/client_cert.html.j2', services=current_app.lenticular_services, client_certs=client_certs)


@frontend_views.route('/client_cert/<service_name>/<fingerprint>')
@login_required
def get_client_cert(service_name, fingerprint):
    service = current_app.lenticular_services[service_name]
    current_app.pki.get_client_cert(current_user, service, fingerprint)
    pass


@frontend_views.route(
        '/client_cert/<service_name>/new',
        methods=['GET', 'POST'])
@login_required
def client_cert_new(service_name):
    service = current_app.lenticular_services[service_name]
    form = ClientCertForm()
    if form.validate_on_submit():
        valid_time = int(form.data['valid_time']) * timedelta(1, 0, 0)
        cert = current_app.pki.signing_publickey(
                current_user,
                service,
                form.data['publickey'],
                valid_time=valid_time)
        return jsonify({
                'status': 'ok',
                'data': {
                    'cert': cert.pem(),
                    'ca_cert': current_app.pki.get_ca_cert_pem(service)
                }})
    elif form.is_submitted():
        return jsonify({
                'status': 'error',
                'errors': form.errors
            })

    return render_template('frontend/client_cert_new.html.j2',
            service=service,
            form=form)


@frontend_views.route('/totp')
@login_required
def totp():
    delete_form = TOTPDeleteForm()
    return render_template('frontend/totp.html.j2', delete_form=delete_form)


@frontend_views.route('/totp/new', methods=['GET','POST'])
@login_required
def totp_new():
    form = TOTPForm()

    if form.validate_on_submit():
        totp = Totp(name=form.data['name'], secret=form.data['secret'])
        if totp.verify(form.data['token']):
            current_user.make_writeable()
            current_user.totps.append(totp)
            current_user._ldap_object.entry_commit_changes()
            return jsonify({
                    'status': 'ok'})
        else:
            return jsonify({
                'status': 'error',
                'errors': [
                    'TOTP Token invalid'
                    ]})
    return render_template('frontend/totp_new.html.j2', form=form)


@frontend_views.route('/totp/<totp_name>/delete', methods=['GET','POST'])
@login_required
def totp_delete(totp_name):
    current_user.make_writeable()
    current_user.totps.delete(totp_name)
    current_user._ldap_object.entry_commit_changes()

    return jsonify({
            'status': 'ok'})
