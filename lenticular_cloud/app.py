from flask.app import Flask
from flask import g, redirect
from flask.helpers import url_for
from jwkest.jwk import RSAKey, rsa_load
from flask_babel import Babel
from flask_login import LoginManager
import time
import subprocess

from pyop.authz_state import AuthorizationState
from pyop.provider import Provider
from pyop.subject_identifier import HashBasedSubjectIdentifierFactory
from pyop.userinfo import Userinfo as _Userinfo
from ldap3 import Connection, Server, ALL

from . import model
from .pki import Pki


def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:10].decode()
    except Exception:
        return ''

def init_oidc_provider(app):
    with app.app_context():
        issuer = url_for('frontend.index')[:-1]
        authentication_endpoint = url_for('oidc_provider.authentication_endpoint')
        jwks_uri = url_for('oidc_provider.jwks_uri')
        token_endpoint = url_for('oidc_provider.token_endpoint')
        userinfo_endpoint = url_for('oidc_provider.userinfo_endpoint')
        registration_endpoint = url_for('oidc_provider.registration_endpoint')
        end_session_endpoint = url_for('auth.logout')

    configuration_information = {
        'issuer': issuer,
        'authorization_endpoint': authentication_endpoint,
        'jwks_uri': jwks_uri,
        'token_endpoint': token_endpoint,
        'userinfo_endpoint': userinfo_endpoint,
        'registration_endpoint': registration_endpoint,
        'end_session_endpoint': end_session_endpoint,
        'scopes_supported': ['openid', 'profile'],
        'response_types_supported': ['code', 'code id_token', 'code token', 'code id_token token'],  # code and hybrid
        'response_modes_supported': ['query', 'fragment'],
        'grant_types_supported': ['authorization_code', 'implicit'],
        'subject_types_supported': ['pairwise'],
        'token_endpoint_auth_methods_supported': ['client_secret_basic', 'client_secret_post'],
        'claims_parameter_supported': True
    }

    from .model_db import db, Client, AuthzCode, AccessToken, RefreshToken, SubjectIdentifier
    from .model import User
    import json
    db.init_app(app)
    with app.app_context():
        db.create_all()

    class SqlAlchemyWrapper(object):
        def __init__(self, cls):
            self._cls = cls
            pass

        def __getitem__(self, item):
            o = self._cls.query.get(item)
            if o is not None:
                return json.loads(o.value)
            else:
                raise KeyError()

        def __setitem__(self, item, value):
            o = self._cls.query.get(item)
            if o is None:
                o = self._cls(key=item)
                db.session.add(o)
            o.value = json.dumps(value)
            db.session.commit()

        def items(self):
            aa = self._cls.query.all()
            return [(a.key, json.loads(a.value)) for a in aa]

        def __contains__(self, item):
            return self._cls.query.get(item) is not None

    class Userinfo(_Userinfo):
        def __init__(self):
            pass

        def __getitem__(self, item):
            return User.query().by_username(item)

        def __contains__(self, item):
            return User.query().by_username(item) is not None

        def get_claims_for(self, user_id, requested_claims):
            user = self[user_id]
            print(f'user {user.username} {requested_claims}')
            claims = {}
            for claim in requested_claims:
                if claim == 'name':
                    claims[claim] = str(user.username)
                elif claim == 'email':
                    claims[claim] = str(user.mail)
                elif claim == 'email_verified':
                    claims[claim] = True
                else:
                    print(f'claim not found {claim}')
            return claims

    client_db = SqlAlchemyWrapper(Client)

    userinfo_db = Userinfo()
    signing_key = RSAKey(key=rsa_load('signing_key.pem'), alg='RS256')
    provider = Provider(
            signing_key,
            configuration_information,
            AuthorizationState(
                HashBasedSubjectIdentifierFactory(app.config['SUBJECT_ID_HASH_SALT']),
                SqlAlchemyWrapper(AuthzCode),
                SqlAlchemyWrapper(AccessToken),
                SqlAlchemyWrapper(RefreshToken),
                SqlAlchemyWrapper(SubjectIdentifier)
                ),
            client_db,
            userinfo_db)

    return provider

def oidc_provider_init_app(name=None):
    name = name or __name__
    app = Flask(name)
    app.config.from_pyfile('application.cfg')
    app.config.from_pyfile('production.cfg')

    app.jinja_env.globals['GIT_HASH'] = get_git_hash()

    #app.ldap_orm = Connection(app.config['LDAP_URL'], app.config['LDAP_BIND_DN'], app.config['LDAP_BIND_PW'], auto_bind=True)
    server = Server(app.config['LDAP_URL'], get_info=ALL)
    app.ldap_conn = Connection(server, app.config['LDAP_BIND_DN'], app.config['LDAP_BIND_PW'], auto_bind=True)
    model.ldap_conn = app.ldap_conn
    model.base_dn = app.config['LDAP_BASE_DN']

    app.babel = Babel(app)
    app.login_manager = LoginManager(app)
    init_login_manager(app)

    from .views import oidc_provider_views, auth_views, frontend_views
    app.register_blueprint(oidc_provider_views)
    app.register_blueprint(auth_views)
    app.register_blueprint(frontend_views)

    @app.before_request
    def befor_request():
        request_start_time = time.time()
        g.request_time = lambda: "%.5fs" % (time.time() - request_start_time)

    # Initialize the oidc_provider after views to be able to set correct urls
    app.provider = init_oidc_provider(app)

    from .translations import init_babel

    init_babel(app)

    app.lenticular_services = {}
    for service_name, service_config in app.config['LENTICULAR_CLOUD_SERVICES'].items():
        app.lenticular_services[service_name] = model.Service.from_config(service_name, service_config)

    app.pki = Pki(app.config['PKI_PATH'], app.config['DOMAIN'])

    return app


def init_login_manager(app):
    @app.login_manager.user_loader
    def user_loader(username):
        return model.User.query().by_username(username)

    @app.login_manager.request_loader
    def request_loader(request):
        pass

    @app.login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('auth.login'))
