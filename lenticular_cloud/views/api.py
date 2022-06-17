import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from flask.typing import ResponseReturnValue

from flask import Blueprint, render_template, request, url_for
import logging
import httpx

from ..model import User
from ..auth_providers import LdapAuthProvider
from ..hydra import hydra_service
from ory_hydra_client.api.admin import introspect_o_auth_2_token
from ory_hydra_client.models import GenericError


api_views = Blueprint('api', __name__, url_prefix='/api')

logger = logging.getLogger(__name__)


@api_views.route('/users', methods=['GET'])
def user_list() -> ResponseReturnValue:
#   if 'authorization' not in request.headers:
#       return '', 403
#   token = request.headers['authorization'].replace('Bearer ', '')
#   token_info = introspect_o_auth_2_token.sync(_client=hydra_service.hydra_client)

#   if token_info is None or isinstance(token_info, GenericError):
#       return 'internal errror', 500

#   if not isinstance(token_info.scope, str) or 'lc_i_userlist' not in token_info.scope.split(' '):
#       return '', 403

    return jsonify([
            {'username': str(user.username), 'email': str(user.email)}
            for user in User.query_().all()])

@api_views.route('/introspect', methods=['POST'])
def introspect() -> ResponseReturnValue:
    token = request.form['token']
    logger.error(f'debug token: {token}')
    resp = httpx.post("https://hydra.cloud.tux.ac/oauth2/introspect", data={'token':token})
    #if token_info is None or isinstance(token_info, GenericError):
    if resp.status_code != 200:
        return jsonify({}), 500
    token_info = resp.json()
    #token_info = introspect_o_auth_2_token.sync(_client=hydra_service, token=token)

    if not token_info['active']:
        return jsonify({'active': False})
    token_info['email'] = token_info['ext']['email']

    logger.error(f'debug: {token_info}')

    return jsonify(token_info)


@api_views.route('email/login', methods=['POST'])
def email_login() -> ResponseReturnValue:
    logger.error(f'{request}')
    logger.error(f'{request.headers}')
    if not request.is_json:
        return jsonify({}), 400
    req_payload = request.get_json()
    logger.error(f'{req_payload}')
    password = req_payload["password"]
    username = req_payload["username"]

    if password == "123456":
        return jsonify({})

    return jsonify({}), 403

