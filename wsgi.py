import logging

from lenticular_cloud.app import create_app

app = create_app()
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    #app.run(ssl_context=('https.crt', 'https.key'), debug=True, host='127.0.0.1')
    app.run(debug=True, host='127.0.0.1', port=9090)
