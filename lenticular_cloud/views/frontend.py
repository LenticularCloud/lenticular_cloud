
from urllib.parse import urlencode, parse_qs

from flask import Blueprint, redirect
from flask import current_app
from flask import jsonify
from flask import render_template, url_for, flash
from flask_login import login_user, logout_user, current_user
from werkzeug.utils import redirect
import logging
from datetime import timedelta
from base64 import b64decode
from flask_dance.consumer import oauth_authorized
from flask_dance.consumer import OAuth2ConsumerBlueprint
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from ..model import db, User, SecurityUser, Totp
from ..form.frontend import ClientCertForm, TOTPForm, \
    TOTPDeleteForm, PasswordChangeForm
from ..auth_providers import LdapAuthProvider

frontend_views = Blueprint('frontend', __name__, url_prefix='')
logger = logging.getLogger(__name__)


def before_request():
    try:
        resp = current_app.oauth.session.get('/userinfo')
        if not current_user.is_authenticated or resp.status_code is not 200:
            return redirect(url_for('oauth.login'))
    except TokenExpiredError:
        return redirect(url_for('oauth.login'))


frontend_views.before_request(before_request)


def init_login_manager(app):
    @app.login_manager.user_loader
    def user_loader(username):
        return User.query_().by_username(username)

    @app.login_manager.request_loader
    def request_loader(_request):
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

        db_user = User.query.get(str(oauth_info["sub"]))

        login_user(SecurityUser(db_user.username))
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
        return redirect(
            f'{current_app.config["HYDRA_PUBLIC_URL"]}/oauth2/sessions/logout')


@frontend_views.route('/', methods=['GET'])
def index():
    return render_template('frontend/index.html.j2')


@frontend_views.route('/client_cert')
def client_cert():
    client_certs = {}
    for service in current_app.lenticular_services.values():
        client_certs[str(service.name)] = \
                current_app.pki.get_client_certs(current_user, service)

    return render_template(
            'frontend/client_cert.html.j2',
            services=current_app.lenticular_services,
            client_certs=client_certs)


@frontend_views.route('/client_cert/<service_name>/<serial_number>')
def get_client_cert(service_name, serial_number):
    service = current_app.lenticular_services[service_name]
    cert = current_app.pki.get_client_cert(
            current_user, service, serial_number)
    return jsonify({
        'data': {
            'pem': cert.pem()}
        })


@frontend_views.route(
        '/client_cert/<service_name>/<serial_number>', methods=['DELETE'])
def revoke_client_cert(service_name, serial_number):
    service = current_app.lenticular_services[service_name]
    cert = current_app.pki.get_client_cert(
            current_user, service, serial_number)
    current_app.pki.revoke_certificate(cert)
    return jsonify({})


@frontend_views.route(
        '/client_cert/<service_name>/new',
        methods=['GET', 'POST'])
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

    return render_template(
            'frontend/client_cert_new.html.j2',
            service=service,
            form=form)


@frontend_views.route('/totp')
def totp():
    delete_form = TOTPDeleteForm()
    return render_template('frontend/totp.html.j2', delete_form=delete_form)


@frontend_views.route('/totp/new', methods=['GET', 'POST'])
def totp_new():
    form = TOTPForm()

    if form.validate_on_submit():
        totp = Totp(name=form.data['name'], secret=form.data['secret'])
        if totp.verify(form.data['token']):
            current_user.totps.append(totp)
            db.session.commit()
            return jsonify({
                    'status': 'ok'})
        else:
            return jsonify({
                'status': 'error',
                'errors': [
                    'TOTP Token invalid'
                    ]})
    return render_template('frontend/totp_new.html.j2', form=form)


@frontend_views.route('/totp/<totp_name>/delete', methods=['GET', 'POST'])
def totp_delete(totp_name):
    totp = Totp.query.filter(Totp.name == totp_name).first()
    db.session.delete(totp)
    db.session.commit()

    return jsonify({
            'status': 'ok'})


@frontend_views.route('/password_change')
def password_change():
    form = PasswordChangeForm()
    return render_template('frontend/password_change.html.j2', form=form)


@frontend_views.route('/password_change', methods=['POST'])
def password_change_post():
    form = PasswordChangeForm()
    if form.validate():
        password_old = str(form.data['password_old'])
        password_new = str(form.data['password_new'])
        if not LdapAuthProvider.check_auth_internal(
                current_user, password_old):
            return jsonify(
                    {'errors': {'password_old': 'Old Password is invalid'}})
        resp = current_user.change_password(password_new)
        if resp:
            print(current_user)
            return jsonify({})
        else:
            return jsonify({'errors': {'internal': 'internal server errror'}})
    return jsonify({'errors': form.errors})


@frontend_views.route('/oauth2_token')
def oauth2_tokens():

    subject = current_app.oauth.session.get('/userinfo').json()['sub']
    consent_sessions = current_app.hydra_api.list_subject_consent_sessions(
                                subject)

    print(consent_sessions)
    return render_template(
            'frontend/oauth2_tokens.html.j2',
            consent_sessions=consent_sessions)


@frontend_views.route('/oauth2_token/<client_id>', methods=['DELETE'])
def oauth2_token_revoke(client_id: str):
    subject = current_app.oauth.session.get('/userinfo').json()['sub']
    current_app.hydra_api.revoke_consent_sessions(
                                subject,
                                client=client_id)

    return jsonify({})
