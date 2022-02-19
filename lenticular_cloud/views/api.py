import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template
from flask.typing import ResponseReturnValue

from flask import Blueprint, render_template, request, url_for
import logging

from ..model import User
from ..auth_providers import LdapAuthProvider
from ..hydra import hydra_service
from ory_hydra_client.api.admin import introspect_o_auth_2_token
from ory_hydra_client.models import GenericError


api_views = Blueprint('api', __name__, url_prefix='/api')


@api_views.route('/users', methods=['GET'])
def user_list() -> ResponseReturnValue:
    if 'authorization' not in request.headers:
        return '', 403
    token = request.headers['authorization'].replace('Bearer ', '')
    token_info = introspect_o_auth_2_token.sync(_client=hydra_service.hydra_client)

    if token_info is None or isinstance(token_info, GenericError):
        return 'internal errror', 500

    if not isinstance(token_info.scope, str) or 'lc_i_userlist' not in token_info.scope.split(' '):
        return '', 403

    return jsonify([
            {'username': str(user.username), 'email': str(user.email)}
            for user in User.query_().all()])
