
from authlib.integrations.base_client.errors import MissingTokenError, InvalidTokenError
from base64 import b64encode, b64decode
from fido2 import cbor
from fido2.client import ClientData
from fido2.ctap2 import AttestationObject, AttestedCredentialData, AuthenticatorData
from flask import Blueprint, Response, redirect, request
from flask import current_app
from flask import jsonify, session, flash
from flask import render_template, url_for
from flask_login import login_user, logout_user, current_user
from http import HTTPStatus
from werkzeug.utils import redirect
import logging
from datetime import timedelta
from base64 import b64decode
from flask.typing import ResponseReturnValue 
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from ory_hydra_client.api.admin import list_subject_consent_sessions, revoke_consent_sessions
from ory_hydra_client.models import GenericError
from urllib.parse import urlencode, parse_qs
from random import SystemRandom
import string
from typing import Optional

from ..model import db, User, SecurityUser, Totp, WebauthnCredential
from ..form.frontend import ClientCertForm, TOTPForm, \
    TOTPDeleteForm, PasswordChangeForm, WebauthnRegisterForm
from ..form.base import  ButtonForm
from ..auth_providers import LdapAuthProvider
from .auth import webauthn
from .oauth2 import redirect_login, oauth2
from ..hydra import hydra_service
from ..pki import pki
from ..lenticular_services import lenticular_services

frontend_views = Blueprint('frontend', __name__, url_prefix='')
logger = logging.getLogger(__name__)


def before_request() -> Optional[ResponseReturnValue]:
    try:
        resp = oauth2.custom.get('/userinfo')
        if not current_user.is_authenticated or resp.status_code != 200:
            logger.info('user not logged in redirect')
            return redirect_login()
    except MissingTokenError:
        logger.info('MissingTokenError redirect user to login')
        return redirect_login()
    except InvalidTokenError:
        logger.info('InvalidTokenError redirect user to login')
        return redirect_login()

    return None


frontend_views.before_request(before_request)


@frontend_views.route('/logout')
def logout() -> ResponseReturnValue:
    logout_user()
    return redirect(
        f'{current_app.config["HYDRA_PUBLIC_URL"]}/oauth2/sessions/logout')


@frontend_views.route('/', methods=['GET'])
def index() -> ResponseReturnValue:
    if 'next_url' in session:
        next_url = session['next_url']
        del session['next_url']
        return redirect(next_url)
    return render_template('frontend/index.html.j2')


@frontend_views.route('/client_cert')
def client_cert() -> ResponseReturnValue:
    client_certs = {}
    for service in lenticular_services.values():
        client_certs[str(service.name)] = \
                pki.get_client_certs(current_user, service)

    return render_template(
            'frontend/client_cert.html.j2',
            services=lenticular_services,
            client_certs=client_certs)


@frontend_views.route('/client_cert/<service_name>/<serial_number>')
def get_client_cert(service_name, serial_number) -> ResponseReturnValue:
    service = lenticular_services[service_name]
    cert = pki.get_client_cert(
            current_user, service, serial_number)
    return jsonify({
        'data': {
            'pem': cert.pem()}
        })


@frontend_views.route(
        '/client_cert/<service_name>/<serial_number>', methods=['DELETE'])
def revoke_client_cert(service_name, serial_number) -> ResponseReturnValue:
    service = lenticular_services[service_name]
    cert = pki.get_client_cert(
            current_user, service, serial_number)
    pki.revoke_certificate(cert)
    return jsonify({})


@frontend_views.route(
        '/client_cert/<service_name>/new',
        methods=['GET', 'POST'])
def client_cert_new(service_name) -> ResponseReturnValue:
    service = lenticular_services[service_name]
    form = ClientCertForm()
    if form.validate_on_submit():
        valid_time = int(form.data['valid_time']) * timedelta(1, 0, 0)
        cert = pki.signing_publickey(
                current_user,
                service,
                form.data['publickey'],
                valid_time=valid_time)
        return jsonify({
                'status': 'ok',
                'data': {
                    'cert': cert.pem(),
                    'ca_cert': pki.get_ca_cert_pem(service)
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

@frontend_views.route('/app_token')
def app_token() -> ResponseReturnValue:
    return

@frontend_views.route('/app_token/<service_name>/new')
def app_token_new(service_name: str) -> ResponseReturnValue:
    return

@frontend_views.route('/app_token/<service_name>/<token_name>')
def app_token_delete(service_name: str, token_name: str) -> ResponseReturnValue:
    return

@frontend_views.route('/totp')
def totp() -> ResponseReturnValue:
    delete_form = TOTPDeleteForm()
    return render_template('frontend/totp.html.j2', delete_form=delete_form)


@frontend_views.route('/totp/new', methods=['GET', 'POST'])
def totp_new() -> ResponseReturnValue:
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
def totp_delete(totp_name) -> ResponseReturnValue:
    totp = Totp.query.filter(Totp.name == totp_name).first()
    db.session.delete(totp)
    db.session.commit()

    return jsonify({
            'status': 'ok'})


@frontend_views.route('/webauthn/list', methods=['GET'])
def webauthn_list_route() -> ResponseReturnValue:
    """list registered credentials for current user"""

    creds = WebauthnCredential.query.all()
    return render_template('frontend/webauthn_list.html', creds=creds, button_form=ButtonForm())


@frontend_views.route('/webauthn/delete/<webauthn_id>', methods=['POST'])
def webauthn_delete_route(webauthn_id: str) -> ResponseReturnValue:
    """delete registered credential"""

    form = ButtonForm()
    if form.validate_on_submit():
        cred = WebauthnCredential.query.filter(WebauthnCredential.id == webauthn_id).one()
        db.session.delete(cred)
        db.session.commit()
        return redirect(url_for('app.webauthn_list_route'))

    return '', HTTPStatus.BAD_REQUEST



def webauthn_credentials(user: User) -> list[AttestedCredentialData]:
    """get and decode all credentials for given user"""
    return [AttestedCredentialData.create(**cbor.decode(cred.credential_data)) for cred in user.webauthn_credentials]


def random_string(length=32) -> str:
    """generates random string"""
    return ''.join([SystemRandom().choice(string.ascii_letters + string.digits) for i in range(length)])


@frontend_views.route('/webauthn/pkcco', methods=['POST'])
def webauthn_pkcco_route() -> ResponseReturnValue:
    """get publicKeyCredentialCreationOptions"""

    user = User.query.get(current_user.id)
    user_handle = random_string()
    exclude_credentials = webauthn_credentials(user)
    pkcco, state = webauthn.register_begin(
        {'id': user_handle.encode('utf-8'), 'name': user.username, 'displayName': user.username},
        exclude_credentials)
    session['webauthn_register_user_handle'] = user_handle
    session['webauthn_register_state'] = state
    return Response(b64encode(cbor.encode(pkcco)).decode('utf-8'), mimetype='text/plain')


@frontend_views.route('/webauthn/register', methods=['GET', 'POST'])
def webauthn_register_route() -> ResponseReturnValue:
    """register credential for current user"""

    user = User.query.get(current_user.id)
    form = WebauthnRegisterForm()
    if form.validate_on_submit():
        try:
            attestation = cbor.decode(b64decode(form.attestation.data))
            auth_data = webauthn.register_complete(
                session.pop('webauthn_register_state'),
                ClientData(attestation['clientDataJSON']),
                AttestationObject(attestation['attestationObject']))

            db.session.add(WebauthnCredential(
                user_id=user.id,
                user_handle=session.pop('webauthn_register_user_handle'),
                credential_data=cbor.encode(auth_data.credential_data.__dict__),
                name=form.name.data))
            db.session.commit()

            return redirect(url_for('app.webauthn_list_route'))
        except (KeyError, ValueError) as e:
            logger.exception(e)
            flash('Error during registration.', 'error')

    return render_template('frontend/webauthn_register.html', form=form)


@frontend_views.route('/password_change')
def password_change() -> ResponseReturnValue:
    form = PasswordChangeForm()
    return render_template('frontend/password_change.html.j2', form=form)


@frontend_views.route('/password_change', methods=['POST'])
def password_change_post() -> ResponseReturnValue:
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
            return jsonify({})
        else:
            return jsonify({'errors': {'internal': 'internal server errror'}})
    return jsonify({'errors': form.errors})


@frontend_views.route('/oauth2_token')
async def oauth2_tokens() -> ResponseReturnValue:

    subject = oauth2.custom.get('/userinfo').json()['sub']
    consent_sessions = await list_subject_consent_sessions.asyncio(subject=subject, _client=hydra_service.hydra_client)
    if consent_sessions is None or isinstance( consent_sessions, GenericError):
       return 'internal error, could not fetch sessions', 500
    return render_template(
            'frontend/oauth2_tokens.html.j2',
            consent_sessions=consent_sessions)


@frontend_views.route('/oauth2_token/<client_id>', methods=['DELETE'])
async def oauth2_token_revoke(client_id: str) -> ResponseReturnValue:
    subject = oauth2.session.get('/userinfo').json()['sub']
    await revoke_consent_sessions.asyncio( _client=hydra_service.hydra_client,
                                subject=subject,
                                client=client_id)

    return jsonify({})
