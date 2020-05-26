from flask import current_app, Blueprint
from cryptography.hazmat.primitives import serialization


pki_views = Blueprint('pki', __name__, url_prefix='/')


@pki_views.route('/<service_name>.crl')
def crl(service_name: str):
    service = current_app.lenticular_services[service_name]
    crl = current_app.pki.get_crl(service)
    return crl.public_bytes(encoding=serialization.Encoding.DER)

