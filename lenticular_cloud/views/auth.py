
from urllib.parse import urlencode, parse_qs

import flask
from flask import Blueprint, redirect
from flask import current_app, session
from flask.templating import render_template
from flask_babel import gettext

from flask import request, url_for
from flask_login import login_required, login_user, logout_user, current_user
import logging
from urllib.parse import urlparse
from base64 import b64decode, b64encode
import http
import crypt

from ..model import db, User, SecurityUser, UserSignUp
from ..form.auth import ConsentForm, LoginForm, RegistrationForm
from ..auth_providers import AUTH_PROVIDER_LIST


auth_views = Blueprint('auth', __name__, url_prefix='/auth')


@auth_views.route('/consent', methods=['GET', 'POST'])
def consent():
    """Always grant consent."""
    # DUMMPY ONLY

    form = ConsentForm()
    remember_for = 60*60*24*30  # remember for 7 days

    consent_request = current_app.hydra_api.get_consent_request(
                                request.args['consent_challenge'])

    requested_scope = consent_request.requested_scope
    requested_audiences = consent_request.requested_access_token_audience

    if form.validate_on_submit() or consent_request.skip:
        user = User.query.get(consent_request.subject)
        token_data = {
            'preferred_username': str(user.username),
            'email': str(user.email),
            'email_verified': True,
        }
        id_token_data = {}
        if 'openid' in requested_scope:
            id_token_data = token_data
        resp = current_app.hydra_api.accept_consent_request(
            consent_request.challenge, body={
                'grant_scope': requested_scope,
                'grant_access_token_audience': requested_audiences,
                'remember': form.data['remember'],
                'remember_for': remember_for,
                'session': {
                    'access_token': token_data,
                    'id_token': id_token_data
                }
            })
        return redirect(resp.redirect_to)
    return render_template(
            'auth/consent.html.j2',
            form=form,
            client=consent_request.client,
            requested_scope=requested_scope,
            requested_audiences=requested_audiences)


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
        user = User.query_().by_username(form.data['name'])
        if user:
            session['username'] = str(user.username)
        else:
            session['user'] = None
        session['auth_providers'] = []
        return redirect(
                url_for('auth.login_auth', login_challenge=login_challenge))
    return render_template('auth/login.html.j2', form=form)


@auth_views.route('/login/auth', methods=['GET', 'POST'])
def login_auth():
    login_challenge = request.args.get('login_challenge')
    login_request = current_app.hydra_api.get_login_request(login_challenge)
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    auth_forms = {}
    user = User.query_().by_username(session['username'])
    for auth_provider in AUTH_PROVIDER_LIST:
        form = auth_provider.get_form()
        if auth_provider.get_name() not in session['auth_providers'] and\
           auth_provider.check_auth(user, form):
            session['auth_providers'].append(auth_provider.get_name())

        if auth_provider.get_name() not in session['auth_providers']:
            auth_forms[auth_provider.get_name()]=form

    if len(session['auth_providers']) >= 2:
        remember_me = True
#       if db_user is None:
#           db_user = User(username=session['username'])
#           db.session.add(db_user)
#           db.session.commit()

        subject = user.id

        resp = current_app.hydra_api.accept_login_request(
            login_challenge, body={
                'subject': subject,
                'remember': remember_me,
            })
        return redirect(resp.redirect_to)
    return render_template('auth/login_auth.html.j2', forms=auth_forms)


@auth_views.route("/logout")
def logout():
    logout_challenge = request.args.get('logout_challenge')
    logout_request = current_app.hydra_api.get_logout_request(logout_challenge)
    resp = current_app.hydra_api.accept_logout_request(logout_challenge)
    # TODO confirm
    return redirect(resp.redirect_to)



@auth_views.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = UserSignUp()
        user.username = form.data['username']
        user.password = crypt.crypt(form.data['password'])
        user.alternative_email = form.data['alternative_email']
        db.session.add(user)
        db.session.commit()

    return render_template('auth/sign_up.html.j2', form=form)
