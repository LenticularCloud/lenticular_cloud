import flask
from flask import Blueprint, redirect, request
from flask import current_app, session
from flask import jsonify
from flask.helpers import make_response
from flask.templating import render_template

from flask import Blueprint, render_template, request, url_for
import logging
import requests

from ..model import User
from ..auth_providers import LdapAuthProvider


api_views = Blueprint('api', __name__, url_prefix='/api')


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
