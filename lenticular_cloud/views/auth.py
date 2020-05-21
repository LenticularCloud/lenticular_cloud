
from urllib.parse import urlencode, parse_qs

import flask
from flask import Blueprint, redirect
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from oic.oic.message import TokenErrorResponse, UserInfoErrorResponse, EndSessionRequest

from pyop.access_token import AccessToken, BearerTokenError
from pyop.exceptions import InvalidAuthenticationRequest, InvalidAccessToken, InvalidClientAuthentication, OAuthError, \
    InvalidSubjectIdentifier, InvalidClientRegistrationRequest
from pyop.util import should_fragment_encode

from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.utils import redirect
import logging
from urllib.parse import urlparse
from base64 import b64decode, b64encode
import http

from ..model import User, SecurityUser
from ..model_db import db, User as DbUser
from ..form.login import LoginForm
from ..auth_providers import AUTH_PROVIDER_LIST


auth_views = Blueprint('auth', __name__, url_prefix='/auth')

@auth_views.route('/consent', methods=['GET', 'POST'])
def consent():
    """Always grant consent."""
    # DUMMPY ONLY

    remember_me = True
    remember_for = 60*60*24*7 # remember for 7 days

    consent_request = current_app.hydra_api.get_consent_request(request.args['consent_challenge'])
    requested_scope = consent_request.requested_scope
    resp = current_app.hydra_api.accept_consent_request(consent_request.challenge, body={
        'grant_scope': requested_scope,
        'remember': remember_me,
        'remember_for': remember_for,
        })
    return redirect(resp.redirect_to)

@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    login_challenge = request.args.get('login_challenge')
    login_request = current_app.hydra_api.get_login_request(login_challenge)


    if login_request.skip:
        resp = current_app.hydra_api.accept_login_request(
            login_challenge,
            body={'subject': login_request.subject})
        return redirect(resp.redirect_to)
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query().by_username(form.data['name'])
        if user:
            session['username'] = str(user.username)
        else:
            session['user'] = None
        session['auth_providers'] = []
        return redirect(url_for('auth.login_auth', login_challenge=login_challenge))
    return render_template('frontend/login.html.j2', form=form)


@auth_views.route('/login/auth', methods=['GET', 'POST'])
def login_auth():
    login_challenge = request.args.get('login_challenge')
    login_request = current_app.hydra_api.get_login_request(login_challenge)
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    auth_forms = {}
    user = User.query().by_username(session['username'])
    for auth_provider in AUTH_PROVIDER_LIST:
        form = auth_provider.get_form()
        if auth_provider.get_name() not in session['auth_providers'] and\
           auth_provider.check_auth(user, form):
            session['auth_providers'].append(auth_provider.get_name())

        if auth_provider.get_name() not in session['auth_providers']:
            auth_forms[auth_provider.get_name()]=form

    if len(session['auth_providers']) >= 2:
        remember_me = True
        db_user = DbUser.query.filter(DbUser.username == session['username']).one_or_none()
        if db_user is None:
            db_user = DbUser(username=session['username'])
            db.session.add(db_user)
            db.session.commit()

        subject = db_user.id

        resp = current_app.hydra_api.accept_login_request(
            login_challenge, body={
                'subject': subject,
                'remember': remember_me})
        return redirect(resp.redirect_to)

        login_user(SecurityUser(session['username']))
        # TODO use this var
        _next = None
        try:
            _next_url = urlparse(b64decode(request.args.get('next')).decode())
            _host_url = urlparse(request.url)
            if _next_url.scheme == _host_url.scheme and _next_url.netloc == _host_url.netloc :
                _next = _next_url.geturl()
        except TypeError:
            _next = None
        return redirect(_next or url_for('frontend.index'))
    return render_template('frontend/login_auth.html.j2', forms=auth_forms)


@auth_views.route("/logout")
def logout():
    logout_challenge = request.args.get('logout_challenge')
    logout_request = current_app.hydra_api.get_logout_request(logout_challenge)
    resp = current_app.hydra_api.accept_logout_request(logout_challenge)
    return redirect(resp.redirect_to)


