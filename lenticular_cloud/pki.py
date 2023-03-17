from flask import Flask
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, dh
from cryptography.x509.oid import NameOID, ExtendedKeyUsageOID
from cryptography.x509 import ObjectIdentifier
from pathlib import Path
import os
import string
import re
import datetime
from dateutil import tz
from operator import attrgetter
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

    def __init__(self):
        self._pki_path = Path()
        self._domain = ""


    def init_app(self, app: Flask) -> None:
        '''
        pki_path: str base path from the pkis
        '''
        self._pki_path = Path(app.root_path) / app.config['PKI_PATH']
        self._domain = app.config['DOMAIN']



    def _init_ca(self, service: Service):
        '''
        '''
        ca_name = service.name

        ca_private_key = self._ensure_private_key(ca_name)
        ca_cert = self._ensure_ca_cert(ca_name, ca_private_key)
        self.update_crl(ca_name)

        pki_path = self._pki_path / ca_name
        if not pki_path.exists():
            pki_path.mkdir()

        return (ca_private_key, ca_cert)

    def get_client_certs(self, user: User, service: Service):
        pki_path = self._pki_path / service.name
        certs = []
        crl = self._load_ca_crl(service.name)
        for cert_path in pki_path.glob(f'{user.username}*.crt.pem'):
            with cert_path.open('rb') as cert_fd:
                cert_data = x509.load_pem_x509_certificate(
                    cert_fd.read(),
                    backend=default_backend())
                revoked = crl.get_revoked_certificate_by_serial_number(
                        cert_data.serial_number) is not None
                cert = Certificate(
                        user.username, service.name, cert_data, revoked)
                certs.append(cert)

        return sorted(certs, key=attrgetter('not_valid_before'), reverse=True)

    def get_crl(self, service: Service):
        return self._load_ca_crl(service.name)

    def get_client_cert(self, user: User, service: Service, serial_number: str) -> Certificate:
        pki_path = self._pki_path / service.name
        cert_path  = pki_path / f'{user.username}-{serial_number}.crt.pem'
        crl = self._load_ca_crl(service.name)
        with cert_path.open('rb') as cert_fd:
            cert_data = x509.load_pem_x509_certificate(
                cert_fd.read(),
                backend=default_backend())
            revoked = crl.get_revoked_certificate_by_serial_number(
                    cert_data.serial_number) is None
            cert = Certificate(user.username, service.name, cert_data, revoked)
            return cert

    def revoke_certificate(self, cert: Certificate):
        ca_private_key = self._ensure_private_key(cert.ca_name)
        self._revoke_cert(ca_private_key, cert)

    def signing_publickey(self, user: User, service: Service, publickey: str, valid_time=DAY*365):
        _public_key = serialization.load_pem_public_key(
                publickey.encode(), backend=default_backend())

        if isinstance(_public_key, dh.DHPublicKey):
            raise AssertionError('key can not be a dsa key')

        ca_private_key, ca_cert = self._init_ca(service)
        ca_name = service.name
        username = str(user.username)
        config = service.pki_config #TODO use this config
        domain = self._domain
        not_valid_before = datetime.datetime.utcnow()

        ca_public_key = ca_private_key.public_key()
        end_entity_cert_builder = x509.CertificateBuilder().\
            subject_name(x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, config['cn'].format(username=username, domain=domain)),
                x509.NameAttribute(NameOID.EMAIL_ADDRESS, config['email'].format(username=username, domain=domain)),
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
                x509.CRLDistributionPoints([
                    x509.DistributionPoint(
                        full_name=[x509.UniformResourceIdentifier(f'http://crl.{self._domain}/{ca_name}.crl')],
                        relative_name=None,
                        crl_issuer=None,
                        reasons=None)
                    ]),
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

        serial_number = f'{end_entity_cert.serial_number:X}'
        end_entity_cert_filename = self._pki_path / ca_name / \
            f'{safe_filename(username)}-{serial_number}.crt.pem'
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

    def _revoke_cert(self, ca_private_key, cert):
        crl = self._load_ca_crl(cert.ca_name)
        builder = self._builder_crl(cert.ca_name, crl)
        revoked_certificate = x509.RevokedCertificateBuilder().serial_number(
                    cert.raw.serial_number
                ).revocation_date(
                    datetime.datetime.now(tz.tzlocal())
                ).build(default_backend())
        builder = builder.add_revoked_certificate(revoked_certificate)
        crl = self._crl_save(cert.ca_name, ca_private_key, builder)
        foobar = crl.get_revoked_certificate_by_serial_number(cert.raw.serial_number)

    def _get_path_crl(self, ca_name):
        return self._pki_path / f'{ca_name}.crl.pem'

    def _crl_save(self, ca_name, private_key, builder):
        crl = builder.sign(
                private_key=private_key,
                algorithm=hashes.SHA256(),
                backend=default_backend()
            )
        ca_crl_filename = self._get_path_crl(ca_name)
        with open(ca_crl_filename, "wb") as ca_crl_file:
            ca_crl_file.write(
                crl.public_bytes(encoding=serialization.Encoding.PEM))
        return crl

    def _builder_crl(self, ca_name, old_crl=None):
            builder = x509.CertificateRevocationListBuilder()
            iname = x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, f'Lenticular Cloud CA - {ca_name}'),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME,
                    'Lenticluar Cloud'),
                x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME,
                    ca_name),
            ])

            builder = builder.issuer_name(iname)
            builder = builder.last_update(datetime.datetime.now(tz.tzlocal()))
            builder = builder.next_update(datetime.datetime.now(tz.tzlocal()) + DAY)
            if old_crl is not None:
                for revoked_certificate in old_crl:
                    builder = builder.add_revoked_certificate(revoked_certificate)

            return builder

    def update_crl(self, ca_name):
        ca_private_key = self._ensure_private_key(ca_name)
        crl = self._load_ca_crl(ca_name)
        builder = self._builder_crl(ca_name, crl)
        return self._crl_save(ca_name, ca_private_key, builder)

    def _load_ca_crl(self, ca_name):
        ca_crl_filename = self._get_path_crl(ca_name)
        if ca_crl_filename.exists():
            with ca_crl_filename.open("rb") as ca_crl_file:
                crl = x509.load_pem_x509_crl(
                    ca_crl_file.read(),
                    backend=default_backend())
                return crl

pki = Pki()
