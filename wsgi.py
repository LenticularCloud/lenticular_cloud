import logging

from lenticular_cloud.app import oidc_provider_init_app

name = 'oidc_provider'
app = oidc_provider_init_app(name)
logging.basicConfig(level=logging.DEBUG)

from flask_debug import Debug
Debug(app)

if __name__ == "__main__":
    app.run(ssl_context=('https.crt', 'https.key'), debug=True, host='::')
