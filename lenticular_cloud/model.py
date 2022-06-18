from flask import current_app
from flask_login import UserMixin
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from collections.abc import MutableSequence
from datetime import datetime
from dateutil import tz
import pyotp
import json
import logging
import crypt
from flask_sqlalchemy import SQLAlchemy, orm
from flask_migrate import Migrate
from datetime import datetime
import uuid
import pyotp
from typing import Optional, Callable
from cryptography.x509 import Certificate as CertificateObj
from sqlalchemy.ext.declarative import DeclarativeMeta

logger = logging.getLogger(__name__)




db = SQLAlchemy()  # type: SQLAlchemy
migrate = Migrate()


BaseModel: DeclarativeMeta = db.Model

class SecurityUser(UserMixin):

    def __init__(self, username):
        self._username = username

    def get_id(self):
        return self._username


class Service(object):

    def __init__(self, name: str):
        self._name = name
        self._client_cert = False
        self._pki_config = {
                    'cn': '{username}',
                    'email': '{username}@{domain}'
                }

    @staticmethod
    def from_config(name, config) -> 'Service':
        """
        """
        service = Service(name)
        if 'client_cert' in config:
            service._client_cert = bool(config['client_cert'])
        if 'pki_config' in config:
            service._pki_config.update(config['pki_config'])

        return service

    @property
    def name(self) -> str:
        return self._name

    @property
    def client_cert(self) -> bool:
        return self._client_cert

    @property
    def pki_config(self) -> dict[str,str]:
        if not self._client_cert:
            raise Exception('invalid call')
        return self._pki_config


class Certificate(object):

    def __init__(self, cn: str, ca_name: str, cert_data: CertificateObj, revoked=False):
        self._cn = cn
        self._ca_name = ca_name
        self._cert_data = cert_data
        self._revoked = revoked
        self._cert_data.not_valid_after.replace(tzinfo=tz.tzutc())
        self._cert_data.not_valid_before.replace(tzinfo=tz.tzutc())

    @property
    def cn(self) -> str:
        return self._cn

    @property
    def ca_name(self) -> str:
        return self._ca_name

    @property
    def not_valid_before(self) -> datetime:
        return self._cert_data.not_valid_before.replace(tzinfo=tz.tzutc()).astimezone(tz.tzlocal()).replace(tzinfo=None)

    @property
    def not_valid_after(self) -> datetime:
        return self._cert_data.not_valid_after.replace(tzinfo=tz.tzutc()).astimezone(tz.tzlocal()).replace(tzinfo=None)

    @property
    def serial_number(self) -> int:
        return self._cert_data.serial_number

    @property
    def serial_number_hex(self) -> str:
        return f'{self._cert_data.serial_number:X}'

    def fingerprint(self, algorithm=hashes.SHA256()) -> bytes:
        return self._cert_data.fingerprint(algorithm)

    @property
    def is_valid(self) -> bool:
        return self.not_valid_after > datetime.now() and not self._revoked

    def pem(self) -> str:
        return self._cert_data.public_bytes(encoding=serialization.Encoding.PEM).decode()

    @property
    def raw(self):
        return self._cert_data

    def __str__(self):
        return f'Certificate(cn={self._cn}, ca_name={self._ca_name}, not_valid_before={self.not_valid_before}, not_valid_after={self.not_valid_after})'


def generate_uuid():
    return str(uuid.uuid4())


class User(BaseModel):
    id = db.Column(
            db.String(length=36), primary_key=True, default=generate_uuid)
    username = db.Column(
            db.String, unique=True, nullable=False)
    password_hashed = db.Column(
            db.String, nullable=False)
    alternative_email = db.Column(
            db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)
    modified_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now, onupdate=datetime.now)
    last_login = db.Column(db.DateTime, nullable=True)

    enabled = db.Column(db.Boolean, nullable=False, default=False)

    totps = db.relationship('Totp', back_populates='user')
    webauthn_credentials = db.relationship('WebauthnCredential', back_populates='user', cascade='delete,delete-orphan', passive_deletes=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def is_authenticated(self) -> bool:
        return True  # TODO

    def get(self, key) -> None:
        print(f'getitem: {key}') # TODO

    @property
    def groups(self) -> list[str]:
        if self.username == 'tuxcoder':
            return [Group(name='admin')]
        else:
            return []

    @property
    def email(self) -> str:
        domain = current_app.config['DOMAIN']
        return f'{self.username}@{domain}'

    def change_password(self, password_new: str) -> bool:
        password_hashed = crypt.crypt(password_new)
        return True

class AppToken(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)


class Totp(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    #last_used = db.Column(db.DateTime, nullable=True)

    user_id = db.Column(
            db.String(length=36),
            db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

    def verify(self, token: str) -> bool:
        totp = pyotp.TOTP(self.secret)
        return totp.verify(token)


class WebauthnCredential(BaseModel):  # pylint: disable=too-few-public-methods
    """Webauthn credential model"""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(length=36), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user_handle = db.Column(db.String(64), nullable=False)
    credential_data = db.Column(db.LargeBinary, nullable=False)
    name = db.Column(db.String(250))
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='webauthn_credentials')


class Group(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

