import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from oic.oic.message import TokenErrorResponse, UserInfoErrorResponse, EndSessionRequest

from flask import Blueprint, render_template, request, url_for
import logging
import requests

from ..model import User
from ..auth_providers import LdapAuthProvider


api_views = Blueprint('api', __name__, url_prefix='/api')

@api_views.route('/userinfo', methods=['GET', 'POST'])
def userinfo():
    if 'authorization' not in request.headers:
        return 'not token found', 400
    token = request.headers['authorization'].replace('Bearer ', '')
    token_info = current_app.hydra_api.introspect_o_auth2_token(token=token)
    if not token_info.active:
        return 'token not valid', 403

    user_db = User.query.get(token_info.sub)
    user = User.query_().by_username(user_db.username)

    public_url = current_app.config.get('HYDRA_PUBLIC_URL')
    r = requests.get(
            f"{public_url}/userinfo",
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

    return jsonify([
            {'username': str(user.username), 'email': str(user.email)}
            for user in User.query_().all()])
