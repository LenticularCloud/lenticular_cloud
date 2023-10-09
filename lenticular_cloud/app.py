from flask.app import Flask
from flask import g
from flask.json.provider import DefaultJSONProvider
import time
import subprocess
from lenticular_cloud.lenticular_services import lenticular_services
import os
import toml
import json
import logging
from uuid import UUID

from pathlib import Path

from .pki import pki
from .hydra import hydra_service
from .translations import init_babel
from .model import db, migrate
from .views import auth_views, frontend_views, init_login_manager, api_views, pki_views, admin_views, oauth2_views

logger = logging.getLogger(__name__)

def get_git_hash():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'])[:10].decode()
    except Exception:
        return ''



class CustomJSONEncoder(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        return super().default(obj)


def create_app_raw(config_files: list[Path]) -> Flask:
    name = "lenticular_cloud"
    app = Flask(name, template_folder='template')
    app.json_provider_class = CustomJSONEncoder
    
    # config
    app.config.from_file('config_development.toml', toml.load)
    for config_file in config_files:
        active_cfg = str(config_file.absolute())
        if active_cfg.endswith(".toml"):
            logger.info(f"load toml config file from {active_cfg}")
            app.config.from_file(active_cfg, toml.load)
        elif active_cfg.endswith(".json"):
            logger.info(f"load json config file from {active_cfg}")
            app.config.from_file(active_cfg, json.load)
        else:
            logger.info(f"load pyfile config file from {active_cfg}")
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
    hydra_service.init_app(app)

    init_login_manager(app) # has to be after hydra_service
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


def create_app() -> Flask:
    evn_var = os.getenv('CONFIG_FILE', None)
    if isinstance(evn_var, str):
        active_cfgs = list(map(Path, evn_var.split(':')))
    else:
        active_cfgs = [ Path() / 'production.toml' ]

    return create_app_raw(active_cfgs)