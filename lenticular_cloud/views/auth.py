
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

from ..model import User, SecurityUser
from ..form.login import LoginForm
from ..auth_providers import AUTH_PROVIDER_LIST
from .oidc import do_logout


auth_views = Blueprint('auth', __name__, url_prefix='')


def init_login_manager(app):
    @app.login_manager.user_loader
    def user_loader(username):
        return User.query().by_username(username)

    @app.login_manager.request_loader
    def request_loader(request):
        pass

    @app.login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login', next=b64encode(request.url.encode())))

@auth_views.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query().by_username(form.data['name'])
        if user:
            session['username'] = str(user.username)
        else:
            session['user'] = None
        session['auth_providers'] = []
        return redirect(url_for('auth.login_auth', next=flask.request.args.get('next')))
        
    return render_template('frontend/login.html.j2', form=form)


@auth_views.route('/login/auth', methods=['GET', 'POST'])
def login_auth():
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
@login_required
def logout():
    logout_user()
    do_logout()
    return redirect(url_for('.login'))

