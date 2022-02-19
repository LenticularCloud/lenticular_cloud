
build-browser-app:
	npm install
	node ./node_modules/webpack-cli/bin/cli.js


server_keys: https.crt https.key
https.key:
	openssl genrsa -passout 'pass:' -out https.key
https.crt: https.key
	openssl req -x509 -key https.key -out https.crt -days 365 -subj "/C=US/ST=Test/L=Test/O=Test/CN=account.example.com" -addext "subjectAltName=DNS:account.example.com" \

clean:
	rm lenticular_cloud/static -rf

run: server_keys
	./venv/bin/gunicorn wsgi:app -b :9090 --certfile https.crt --keyfile https.key
