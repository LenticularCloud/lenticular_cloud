import logging
from lenticular_cloud.app import oidc_provider_init_app

name = 'oidc_provider'
app = oidc_provider_init_app(name)
logging.basicConfig(level=logging.DEBUG)

with app.context():

