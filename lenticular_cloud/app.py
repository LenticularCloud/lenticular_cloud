from flask.app import Flask
from flask import g, redirect, request
from flask.helpers import url_for
import time
import subprocess
from ory_hydra_client import Client
import os

from ldap3 import Connection, Server, ALL

from . import model
from .pki import Pki
from .hydra import hydra_service
from .translations import init_babel


def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:10].decode()
    except Exception:
        return ''


def create_app() -> Flask:
    name = "lenticular_cloud"
    app = Flask(name, template_folder='template')
    app.config.from_pyfile('application.cfg')
    active_cfg = os.getenv('CONFIG_FILE', 'production.cfg')
    app.config.from_pyfile(active_cfg)

    app.jinja_env.globals['GIT_HASH'] = get_git_hash()

    #app.ldap_orm = Connection(app.config['LDAP_URL'], app.config['LDAP_BIND_DN'], app.config['LDAP_BIND_PW'], auto_bind=True)
    server = Server(app.config['LDAP_URL'], get_info=ALL)
    app.ldap_conn = Connection(server, app.config['LDAP_BIND_DN'], app.config['LDAP_BIND_PW'], auto_bind="DEFAULT")
    model.ldap_conn = app.ldap_conn
    model.base_dn = app.config['LDAP_BASE_DN']

    from .model import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)
#    with app.app_context():
#        db.create_all()

    init_babel(app)

    #init hydra admin api
#    hydra_config = hydra.Configuration(
#                        host=app.config['HYDRA_ADMIN_URL'],
#                        username=app.config['HYDRA_ADMIN_USER'],
#                        password=app.config['HYDRA_ADMIN_PASSWORD'])
    hydra_service.set_hydra_client(Client(base_url=app.config['HYDRA_ADMIN_URL']))

    from .views import auth_views, frontend_views, init_login_manager, api_views, pki_views, admin_views, oauth2_views
    init_login_manager(app)
    #oauth2.init_app(app)
    app.register_blueprint(auth_views)
    app.register_blueprint(frontend_views)
    app.register_blueprint(api_views)
    app.register_blueprint(pki_views)
    app.register_blueprint(admin_views)
    app.register_blueprint(oauth2_views)

    @app.before_request
    def befor_request():
        request_start_time = time.time()
        g.request_time = lambda: "%.5fs" % (time.time() - request_start_time)

    app.lenticular_services = {}
    for service_name, service_config in app.config['LENTICULAR_CLOUD_SERVICES'].items():
        app.lenticular_services[service_name] = model.Service.from_config(service_name, service_config)

    app.pki = Pki(app.config['PKI_PATH'], app.config['DOMAIN'])

    return app

