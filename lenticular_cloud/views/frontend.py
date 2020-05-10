
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

from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.utils import redirect
import logging
from datetime import timedelta
import pyotp


from ..model import User, SecurityUser, Totp
from ..form.login import LoginForm
from ..form.frontend import ClientCertForm, TOTPForm, TOTPDeleteForm
from ..auth_providers import AUTH_PROVIDER_LIST


frontend_views = Blueprint('frontend', __name__, url_prefix='')


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
