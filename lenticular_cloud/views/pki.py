from flask import Blueprint
from cryptography.hazmat.primitives import serialization
from ..lenticular_services import lenticular_services
from ..pki import pki


pki_views = Blueprint('pki', __name__, url_prefix='/')


@pki_views.route('/<service_name>.crl')
def crl(service_name: str):
    service = lenticular_services[service_name]
    crl = pki.get_crl(service)
    return crl.public_bytes(encoding=serialization.Encoding.DER)

