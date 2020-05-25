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
from cryptography.hazmat.primitives import serialization

from ..model import User, SecurityUser
from ..model_db import User as DbUser
from ..form.login import LoginForm
from ..auth_providers import LdapAuthProvider


pki_views = Blueprint('pki', __name__, url_prefix='/')

@pki_views.route('/<service_name>.crl')
def crl(service_name: str):
    service = current_app.lenticular_services[service_name]
    crl = current_app.pki.get_crl(service)
    return crl.public_bytes(encoding=serialization.Encoding.DER)

