from flask.app import Flask
from flask import g, redirect, request
from flask.helpers import url_for
import time
import subprocess
from lenticular_cloud.lenticular_services import lenticular_services
from ory_hydra_client import Client
import os

from pathlib import Path

from .pki import pki
from .hydra import hydra_service
from .translations import init_babel
from .model import db, migrate
from .views import auth_views, frontend_views, init_login_manager, api_views, pki_views, admin_views, oauth2_views


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

    db.init_app(app)
    migration_dir = Path(app.root_path) / 'migrations'
    migrate.init_app(app, db, directory=str(migration_dir))
#    with app.app_context():
#        db.create_all()

    init_babel(app)

    #init hydra admin api
#    hydra_config = hydra.Configuration(
#                        host=app.config['HYDRA_ADMIN_URL'],
#                        username=app.config['HYDRA_ADMIN_USER'],
#                        password=app.config['HYDRA_ADMIN_PASSWORD'])
    hydra_service.set_hydra_client(Client(base_url=app.config['HYDRA_ADMIN_URL']))

    init_login_manager(app)
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

    lenticular_services.init_app(app)

    pki.init_app(app)

    return app

