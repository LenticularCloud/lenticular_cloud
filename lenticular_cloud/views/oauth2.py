from authlib.integrations.flask_client import OAuth
from authlib.integrations.base_client.errors import MismatchingStateError
from flask import Flask, Blueprint, Response, session, request, redirect, url_for
from flask_login import login_user, logout_user, current_user
from flask.typing import ResponseReturnValue
from flask_login import LoginManager
from typing import Optional
from werkzeug.wrappers.response import Response as WerkzeugResponse
import logging

from ..model import User, SecurityUser
from ..hydra import hydra_service

logger = logging.getLogger(__name__)

def fetch_token(name: str) -> Optional[dict]:
    token = session.get('token', None)
    if isinstance(token, dict):
        return token
    return None

oauth2 = OAuth(fetch_token=fetch_token)

oauth2_views = Blueprint('oauth2', __name__, url_prefix='/oauth')

login_manager = LoginManager()

def redirect_login() -> ResponseReturnValue:
    logout_user()
    session['next_url'] = request.path
    redirect_uri = url_for('oauth2.authorized', _external=True)
    response = oauth2.custom.authorize_redirect(redirect_uri)
    if not isinstance(response, WerkzeugResponse):
        raise RuntimeError("invalid redirect")
    return response


@oauth2_views.route('/authorized')
def authorized() -> ResponseReturnValue:
    try:
        token = oauth2.custom.authorize_access_token()
    except MismatchingStateError:
        logger.warning("MismatchingStateError redirect user")
        return redirect(url_for('oauth2.login'))
    if token is None:
        return 'bad request', 400
    session['token'] = token
    userinfo = oauth2.custom.get('/userinfo').json()
    user = User.query.get(str(userinfo["sub"])) # type: Optional[User]
    if user is None:
        return "user not found", 404
    logger.info(f"user `{user.username}` successfully logged in")
    login_user(SecurityUser(user.username))

    next_url = request.args.get('next_url')
    if next_url is None:
        next_url = '/'
    return redirect(next_url)


@oauth2_views.route('login')
def login() -> ResponseReturnValue:
    redirect_uri = url_for('.authorized', _external=True)
    response = oauth2.custom.authorize_redirect(redirect_uri)
    if not isinstance(response, WerkzeugResponse):
        raise RuntimeError("invalid redirect")
    return response


@login_manager.user_loader
def user_loader(username) -> Optional[User]:
    user =  User.query.filter_by(username=username).first() # type: Optional[User]
    if isinstance(user, User):
        return user
    else:
        return None

@login_manager.request_loader
def request_loader(_request):
    pass

@login_manager.unauthorized_handler
def unauthorized() -> Optional[User]:
    pass

def init_login_manager(app: Flask) -> None:

    base_url = app.config['HYDRA_PUBLIC_URL']
    if not isinstance(base_url, str):
        raise RuntimeError("HYDRA_PUBLIC_URL not set")

    oauth2.register(
        name="custom",
        client_id=hydra_service.client_id,
        client_secret=app.config['OAUTH_SECRET'],
        server_metadata_url=f'{base_url}/.well-known/openid-configuration',
        access_token_url=f"{base_url}/oauth2/token",
        authorize_url=f"{base_url}/oauth2/auth",
        api_base_url=base_url,

        client_kwargs={'scope': ' '.join(['openid', 'profile', 'manage'])},
    )
    oauth2.init_app(app)
    login_manager.init_app(app)


