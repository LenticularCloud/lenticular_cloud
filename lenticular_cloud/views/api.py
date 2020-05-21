import flask
from flask import Blueprint, redirect, request
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
import ory_hydra_client as hydra
from requests_oauthlib.oauth2_session import OAuth2Session
import requests

from ..model import User, SecurityUser
from ..model_db import User as DbUser
from ..form.login import LoginForm
from ..auth_providers import LdapAuthProvider


api_views = Blueprint('api', __name__, url_prefix='/api')

@api_views.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    token = request.headers['authorization'].replace('Bearer ', '')
    token_info = current_app.hydra_api.introspect_o_auth2_token(token=token)

    user_db = DbUser.query.get(token_info.sub)
    user = User.query().by_username(user_db.username)

    r = requests.get(
            "http://127.0.0.1:4444/userinfo",
            headers={
                'authorization': request.headers['authorization']})
    userinfo = r.json()
    scopes = token_info.scope.split(' ')
    if 'email' in scopes:
        userinfo['email'] = str(user.email)
    if 'profile' in scopes:
        userinfo['username'] = str(user.username)
    print(userinfo)
    return jsonify(userinfo)


@api_views.route('/users', methods=['GET'])
def user_list():
    if 'authorization' not in request.headers:
        return '', 403
    token = request.headers['authorization'].replace('Bearer ', '')
    token_info = current_app.hydra_api.introspect_o_auth2_token(token=token)

    if 'lc_i_userlist' not in token_info.scope.split(' '):
        return '', 403

    return jsonify([{'username': str(user.username), 'email': str(user.email)}
            for user in User.query().all()])
