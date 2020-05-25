import logging

from lenticular_cloud.app import init_app

name = 'oidc_provider'
app = init_app(name)
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    #app.run(ssl_context=('https.crt', 'https.key'), debug=True, host='127.0.0.1')
    app.run(debug=True, host='127.0.0.1', port=9090)
