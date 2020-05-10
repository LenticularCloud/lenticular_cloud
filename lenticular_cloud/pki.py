from flask import current_app
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.x509 import ObjectIdentifier
from pathlib import Path
import os
import string
import re
import datetime
import logging

from .model import Service, User, Certificate


logger = logging.getLogger(__name__)

# partial source from https://github.com/Snawoot/quickcerts
# MIT (C) Snawoot

DAY = datetime.timedelta(1, 0, 0)
CA_FILENAME = 'ca'
KEY_EXT = 'key'
CERT_EXT = 'pem'
E = 65537


safe_symbols = set(string.ascii_letters + string.digits + '-.')


def safe_filename(name):
    return "".join(c if c in safe_symbols else '_' for c in name)


class Pki(object):

    def __init__(self, pki_path: str, domain: str):
        '''
        pki_path: str base path from the pkis
        '''
        self._pki_path = Path(pki_path)
        self._domain = domain


    def _init_ca(self, service: Service):
        '''
        '''
        ca_name = service.name

        ca_private_key = self._ensure_private_key(ca_name)
        ca_cert = self._ensure_ca_cert(ca_name, ca_private_key)

        pki_path = self._pki_path / ca_name
        if not pki_path.exists():
            pki_path.mkdir()

        return (ca_private_key, ca_cert)

    def get_client_certs(self, user: User, service: Service):
        pki_path = self._pki_path / service.name
        certs = []
        for cert_path in pki_path.glob(f'{user.username}*.crt.pem'):
            print(cert_path)
            with cert_path.open('rb') as cert_fd:
                cert_data = x509.load_pem_x509_certificate(
                    cert_fd.read(),
                    backend=default_backend())
                cert = Certificate(user.username, service.name, cert_data)
                certs.append(cert)
        return certs

    def signing_publickey(self, user: User, service: Service, publickey: str, valid_time=DAY*365):
        _public_key = serialization.load_pem_public_key(
                publickey.encode(), backend=default_backend())

        ca_private_key, ca_cert = self._init_ca(service)
        ca_name = service.name
        username = str(user.username)
        config = service.pki_config #TODO use this config
        domain = self._domain
        not_valid_before = datetime.datetime.now()

        ca_public_key = ca_private_key.public_key()
        end_entity_cert_builder = x509.CertificateBuilder().\
            subject_name(x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, username),
                x509.NameAttribute(NameOID.EMAIL_ADDRESS, f'{username}@jabber.{domain}'),
            ])).\
            issuer_name(ca_cert.subject).\
            not_valid_before(not_valid_before).\
            not_valid_after(not_valid_before + valid_time).\
            serial_number(x509.random_serial_number()).\
            public_key(_public_key).\
            add_extension(
                x509.SubjectAlternativeName([
                    x509.DNSName(f'{username}'),
                    ]),
                critical=False).\
            add_extension(
                x509.BasicConstraints(ca=False, path_length=None),
                critical=True).\
            add_extension(
                x509.KeyUsage(digital_signature=True,
                              content_commitment=True,  # False
                              key_encipherment=True,
                              data_encipherment=False,
                              key_agreement=False,
                              key_cert_sign=False,
                              crl_sign=False,
                              encipher_only=False,
                              decipher_only=False),
                critical=True).\
            add_extension(
                x509.ExtendedKeyUsage([
                    ExtendedKeyUsageOID.CLIENT_AUTH,
                    ExtendedKeyUsageOID.SERVER_AUTH,
                ]), critical=False).\
            add_extension(
                x509.AuthorityKeyIdentifier.from_issuer_public_key(ca_public_key),
                critical=False).\
            add_extension(
                x509.SubjectKeyIdentifier.from_public_key(_public_key),
                critical=False).\
            add_extension(
                x509.AuthorityInformationAccess([
                    x509.AccessDescription(
                        access_method=x509.AuthorityInformationAccessOID.CA_ISSUERS,
                        access_location=x509.UniformResourceIdentifier(f'https://www.{self._domain}')),
                    x509.AccessDescription(
                        access_method=x509.AuthorityInformationAccessOID.OCSP,
                        access_location=x509.UniformResourceIdentifier(f'http://ocsp.{self._domain}/{ca_name}/'))
                    ]),
                critical=False)

        end_entity_cert = end_entity_cert_builder.\
            sign(
                private_key=ca_private_key,
                algorithm=hashes.SHA256(),
                backend=default_backend()
            )

        fingerprint =end_entity_cert.fingerprint(hashes.SHA256()).hex()
        end_entity_cert_filename = self._pki_path / ca_name / \
            f'{safe_filename(username)}-{fingerprint}.crt.pem'
        # save cert
        with end_entity_cert_filename.open("wb") as end_entity_cert_file:
            end_entity_cert_file.write(
                end_entity_cert.public_bytes(encoding=serialization.Encoding.PEM))

        return Certificate(user.username, service.name, end_entity_cert)

    def get_ca_cert_pem(self, service: Service):
        ca_private_key, ca_cert = self._init_ca(service)
        return ca_cert.public_bytes(encoding=serialization.Encoding.PEM).decode()

    def _ensure_private_key(self, name, key_size=4096):
        key_filename = self._pki_path / f'{safe_filename(name)}.key.pem'
        if key_filename.exists():
            with open(key_filename, "rb") as key_file:
                private_key = serialization.load_pem_private_key(key_file.read(),
                    password=None, backend=default_backend())
        else:
            logger.info(f'Generate new Private key for {name}')
            private_key = rsa.generate_private_key(public_exponent=E,
                key_size=key_size, backend=default_backend())
            with key_filename.open('wb') as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))
        return private_key

    def _ensure_ca_cert(self, ca_name, ca_private_key):
        ca_cert_filename =self._pki_path / f'{ca_name}.crt.pem'
        ca_public_key = ca_private_key.public_key()
        if ca_cert_filename.exists():
            with ca_cert_filename.open("rb") as ca_cert_file:
                ca_cert = x509.load_pem_x509_certificate(
                    ca_cert_file.read(),
                    backend=default_backend())
        else:
            logger.info(f'Generate new Certificate key for {ca_name}')
            iname = x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, f'Lenticular Cloud CA - {ca_name}'),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME,
                    'Lenticluar Cloud'),
                x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                    ca_name),
            ])
            ca_cert = x509.CertificateBuilder().\
                subject_name(iname).\
                issuer_name(iname).\
                not_valid_before(datetime.datetime.today() - DAY).\
                not_valid_after(datetime.datetime.today() + 3650 * DAY).\
                serial_number(x509.random_serial_number()).\
                public_key(ca_public_key).\
                add_extension(
                    x509.BasicConstraints(ca=True, path_length=None),
                    critical=True).\
                add_extension(
                    x509.KeyUsage(digital_signature=False,
                                  content_commitment=False,
                                  key_encipherment=False,
                                  data_encipherment=False,
                                  key_agreement=False,
                                  key_cert_sign=True,
                                  crl_sign=True,
                                  encipher_only=False,
                                  decipher_only=False),
                    critical=True).\
                add_extension(
                    x509.SubjectKeyIdentifier.from_public_key(ca_public_key),
                    critical=False).\
                sign(
                    private_key=ca_private_key,
                    algorithm=hashes.SHA256(),
                    backend=default_backend()
                )
            with open(ca_cert_filename, "wb") as ca_cert_file:
                ca_cert_file.write(
                    ca_cert.public_bytes(encoding=serialization.Encoding.PEM))
        assert isinstance(ca_cert, x509.Certificate)
        return ca_cert
