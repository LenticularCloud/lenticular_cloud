from flask import Flask
from .model import Service
import logging

logger = logging.getLogger(__name__)


class LenticularServices(dict):

    def init_app(self, app: Flask) -> None:
        for service_name, service_config in app.config['LENTICULAR_CLOUD_SERVICES'].items():
            self[service_name] = Service.from_config(service_name, service_config)


lenticular_services = LenticularServices()