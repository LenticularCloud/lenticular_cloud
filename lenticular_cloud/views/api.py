import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from flask.typing import ResponseReturnValue

from flask import Blueprint, render_template, request, url_for
from datetime import datetime
from typing import Optional, Any
import logging
import httpx
import secrets

from ..model import db, User
from ..hydra import hydra_service
from ..lenticular_services import lenticular_services
from ory_hydra_client.api.o_auth_2 import introspect_o_auth_2_token
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
            for user in User.query.all()])

@api_views.route('/introspect', methods=['POST'])
def introspect() -> ResponseReturnValue:
    token = request.form['token'] # type: Optional[str]
    resp = httpx.post("https://hydra.cloud.tux.ac/oauth2/introspect", data={'token':token})
    if resp.status_code != 200:
        return jsonify({}), 500
    token_info = resp.json()

    if not token_info['active']:
        return jsonify({'active': False})
    token_info['email'] = token_info['ext']['email']


    return jsonify(token_info)


# @api_views.route('/login/<service_name>', methods=['POST'])
# def email_login(service_name: str) -> ResponseReturnValue:
#     if service_name not in lenticular_services:
#         return '', 404
#     service = lenticular_services[service_name]

#     if not request.is_json:
#         return jsonify({}), 400
#     req_payload = request.get_json() # type: Any

#     if not isinstance(req_payload, dict):
#         return 'bad request', 400

#     password = req_payload["password"]
#     username = req_payload["username"]

#     if '@' in username:
#         username = username.split('@')[0]

#     user = User.query.filter_by(username=username.lower()).first() # type: Optional[User]
#     if user is None:
#         logger.warning(f'login with invalid username')
#         return jsonify({}), 403

#     for app_token in user.get_token_by_name(service):
#         if secrets.compare_digest(password, app_token.token):
#             app_token.last_used = datetime.now()
#             db.session.commit()
#             return jsonify({'username': user.username}), 200

#     logger.warning(f'login with invalid password for {username}')
#     return jsonify({}), 403

