
from urllib.parse import urlencode, parse_qs

import flask
from flask import Blueprint, redirect, flash, current_app, session
from flask.templating import render_template
from flask_babel import gettext
from flask.typing import ResponseReturnValue

from flask import request, url_for, jsonify
from flask_login import login_required, login_user, logout_user, current_user
import logging
from urllib.parse import urlparse
from base64 import b64decode, b64encode
import http
import crypt
from datetime import datetime
import logging
import json
from ory_hydra_client.api.o_auth_2 import get_o_auth_2_consent_request, accept_o_auth_2_consent_request, accept_o_auth_2_login_request, get_o_auth_2_login_request, accept_o_auth_2_login_request, accept_o_auth_2_logout_request, get_o_auth_2_login_request
from ory_hydra_client import models as ory_hydra_m
from ory_hydra_client.models import TheRequestPayloadUsedToAcceptALoginOrConsentRequest, TheRequestPayloadUsedToAcceptAConsentRequest, GenericError
from typing import Optional
from uuid import uuid4

from ..model import db, User, SecurityUser
from ..form.auth import ConsentForm, LoginForm, RegistrationForm
from ..auth_providers import AUTH_PROVIDER_LIST
from ..hydra import hydra_service
from ..wrapped_fido2_server import WrappedFido2Server


logger = logging.getLogger(__name__)

auth_views = Blueprint('auth', __name__, url_prefix='/auth')
webauthn = WrappedFido2Server()


@auth_views.route('/consent', methods=['GET', 'POST'])
async def consent() -> ResponseReturnValue:
    """Always grant consent."""
    # DUMMPY ONLY

    form = ConsentForm()
    remember_for = 60*60*24*30  # remember for 30 days

    #try:
    consent_request = await get_o_auth_2_consent_request.asyncio(consent_challenge=request.args['consent_challenge'],_client=hydra_service.hydra_client)

    if consent_request is None or isinstance( consent_request, ory_hydra_m.OAuth20RedirectBrowserTo):
       return redirect(url_for('frontend.index'))

    requested_scope = consent_request.requested_scope
    requested_audiences = consent_request.requested_access_token_audience

    if form.validate_on_submit() or consent_request.skip:
        user = User.query.get(consent_request.subject) # type: Optional[User]
        if user is None:
            return 'internal error', 500
        access_token = {
            'name': str(user.username),
            'preferred_username': str(user.username),
            'username': str(user.username),
            'email': str(user.email),
            'email_verified': True,
            #'given_name': str(user.username),
            #'family_name': '-',
            'groups': [group.name for group in user.groups]
        }
        id_token = {}
        if isinstance(requested_scope, list) and 'openid' in requested_scope:
            id_token = access_token
        body = TheRequestPayloadUsedToAcceptAConsentRequest(
                grant_scope= requested_scope,
                grant_access_token_audience= requested_audiences,
                remember= form.data['remember'],
                remember_for= remember_for,
                session= ory_hydra_m.PassSessionDataToAConsentRequest(
                    access_token= access_token,
                    id_token= id_token
                )
        )
        resp = await accept_o_auth_2_consent_request.asyncio(_client=hydra_service.hydra_client,
            json_body=body,
            consent_challenge=consent_request.challenge)
        if resp is None or isinstance( resp, GenericError):
            return 'internal error, could not forward request', 503
        return redirect(resp.redirect_to)
    return render_template(
            'auth/consent.html.j2',
            form=form,
            client=consent_request.client,
            requested_scope=requested_scope,
            requested_audiences=requested_audiences)


@auth_views.route('/login', methods=['GET', 'POST'])
async def login() -> ResponseReturnValue:
    login_challenge = request.args.get('login_challenge')
    if login_challenge is None:
        return 'login_challenge missing', 400
    login_request = await get_o_auth_2_login_request.asyncio(_client=hydra_service.hydra_client, login_challenge=login_challenge)
    if login_request is None or isinstance( login_request, ory_hydra_m.OAuth20RedirectBrowserTo):
        logger.exception("could not fetch login request")
        return redirect(url_for('frontend.index'))

    if login_request.skip:
        resp = await accept_o_auth_2_login_request.asyncio(_client=hydra_service.hydra_client,
            login_challenge=login_challenge,
            json_body=ory_hydra_m.HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest(subject=login_request.subject))
        if resp is None or isinstance( resp, GenericError):
            return 'internal error, could not forward request', 503

        return redirect(resp.redirect_to)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.data['name']).first() # type: Optional[User]
        if user:
            session['username'] = str(user.username)
        else:
            session['user'] = None
        session['auth_providers'] = []
        return redirect(
                url_for('auth.login_auth', login_challenge=login_challenge))
    return render_template('auth/login.html.j2', form=form)


@auth_views.route('/login/auth', methods=['GET', 'POST'])
async def login_auth() -> ResponseReturnValue:
    login_challenge = request.args.get('login_challenge')
    if login_challenge is None:
        return 'missing login_challenge, bad request', 400
    login_request = await get_o_auth_2_login_request.asyncio(_client=hydra_service.hydra_client, login_challenge=login_challenge)
    if login_request is None:
        return redirect(url_for('frontend.index'))

    if 'username' not in session:
        return redirect(url_for('auth.login'))
    auth_forms = {}
    user = User.query.filter_by(username=session['username']).first_or_404()
    for auth_provider in AUTH_PROVIDER_LIST:
        form = auth_provider.get_form()
        if auth_provider.get_name() not in session['auth_providers'] and\
           auth_provider.check_auth(user, form):
            session['auth_providers'].append(auth_provider.get_name())
            session.modified = True

        if auth_provider.get_name() not in session['auth_providers']:
            auth_forms[auth_provider.get_name()]=form

    if len(session['auth_providers']) >= 2:
        remember_me = True
#       if db_user is None:
#           db_user = User(username=session['username'])
#           db.session.add(db_user)
#           db.session.commit()

        subject = str(user.id)
        user.last_login = datetime.now()
        db.session.commit()
        resp = await accept_o_auth_2_login_request.asyncio(_client=hydra_service.hydra_client,
            login_challenge=login_challenge, json_body=ory_hydra_m.HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest(
                subject=subject,
                remember=remember_me,
            ))
        if resp is None or isinstance( resp, GenericError):
            return 'internal error, could not forward request', 503
        return redirect(resp.redirect_to)
    return render_template('auth/login_auth.html.j2', forms=auth_forms)



@auth_views.route('/webauthn/pkcro', methods=['POST'])
def webauthn_pkcro_route() -> ResponseReturnValue:
    """login webauthn pkcro route"""
    return '', 404

    user = User.query.filter(User.id == session.get('webauthn_login_user_id')).one() #type: User
    form = ButtonForm()
    if user and form.validate_on_submit():
        pkcro, state = webauthn.authenticate_begin(webauthn_credentials(user))
        session['webauthn_login_state'] = state
        return Response(b64encode(cbor.encode(pkcro)).decode('utf-8'), mimetype='text/plain')

    return '', HTTPStatus.BAD_REQUEST


@auth_views.route("/logout")
async def logout() -> ResponseReturnValue:
    logout_challenge = request.args.get('logout_challenge')
    if logout_challenge is None:
        return 'invalid request, logout_challenge not set', 400
    # TODO confirm
    resp = await accept_o_auth_2_logout_request.asyncio(_client=hydra_service.hydra_client, logout_challenge=logout_challenge)
    if resp is None or isinstance( resp, GenericError):
        return 'internal error, could not forward request', 503
    return redirect(resp.redirect_to)


@auth_views.route("/error", methods=["GET"])
def auth_error() -> ResponseReturnValue:
    error = request.args.get('error')
    error_description = request.args.get('error_description')

    return render_template('auth/error.html.j2', error=error, error_description=error_description)


@auth_views.route("/sign_up", methods=["GET"])
def sign_up():
    form = RegistrationForm()
    return render_template('auth/sign_up.html.j2', form=form)

@auth_views.route("/sign_up", methods=["POST"])
def sign_up_submit():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        user.id = uuid4()
        user.username = form.data['username']
        user.password_hashed = crypt.crypt(form.data['password'])
        user.alternative_email = form.data['alternative_email']
        db.session.add(user)
        db.session.commit()
        return jsonify({})
    return jsonify({
            'status': 'error',
            'errors': form.errors
        })


@auth_views.route("/oob", methods=["GET"])
def oob_token():

    token_info = {
        'code': request.args.get('code', default="", type=str),
        'scope': request.args.get('scope', default="", type=str),
        'state': request.args.get('state', default="", type=str),
    }

    return render_template('auth/oob.html.j2', token_info=token_info)
