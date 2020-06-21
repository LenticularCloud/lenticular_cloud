from flask.app import Flask
from flask import g, redirect, request
from flask.helpers import url_for
from jwkest.jwk import RSAKey, rsa_load
from flask_babel import Babel
from flask_login import LoginManager
import time
import subprocess
import ory_hydra_client as hydra

from ldap3 import Connection, Server, ALL

from . import model
from .pki import Pki


def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:10].decode()
    except Exception:
        return ''


def init_oauth2(app):
    pass



def init_app(name=None):
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

    from .model import db
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.babel = Babel(app)
    init_oauth2(app)
    app.login_manager = LoginManager(app)

    #init hydra admin api
    hydra_config = hydra.Configuration(
                        app.config['HYDRA_ADMIN_URL'],
                        username=app.config['HYDRA_ADMIN_USER'],
                        password=app.config['HYDRA_ADMIN_PASSWORD'])
    hydra_client = hydra.ApiClient(hydra_config)
    app.hydra_api = hydra.AdminApi(hydra_client)

    from .views import auth_views, frontend_views, init_login_manager, api_views, pki_views, admin_views
    init_login_manager(app)
    app.register_blueprint(auth_views)
    app.register_blueprint(frontend_views)
    app.register_blueprint(api_views)
    app.register_blueprint(pki_views)
    app.register_blueprint(admin_views)

    @app.before_request
    def befor_request():
        request_start_time = time.time()
        g.request_time = lambda: "%.5fs" % (time.time() - request_start_time)

    from .translations import init_babel

    init_babel(app)

    app.lenticular_services = {}
    for service_name, service_config in app.config['LENTICULAR_CLOUD_SERVICES'].items():
        app.lenticular_services[service_name] = model.Service.from_config(service_name, service_config)

    app.pki = Pki(app.config['PKI_PATH'], app.config['DOMAIN'])

    return app

