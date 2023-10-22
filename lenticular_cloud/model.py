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
import secrets
import string
from sqlalchemy import null
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column, relationship, declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model, DefaultMeta
from flask_sqlalchemy.extension import _FSAModel
from flask_migrate import Migrate
from datetime import datetime
import uuid
from typing import Iterator, Optional, List, Dict, Tuple, Any, Type, TYPE_CHECKING
from cryptography.x509 import Certificate as CertificateObj
from sqlalchemy.ext.declarative import DeclarativeMeta

logger = logging.getLogger(__name__)




db = SQLAlchemy()
migrate = Migrate()

class BaseModelIntern(MappedAsDataclass, DeclarativeBase):
    pass

if TYPE_CHECKING:
    class BaseModel (_FSAModel,BaseModelIntern):
        pass
else:
    BaseModel: Type[_FSAModel] = db.Model

class ModelUpdatedMixin:
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now(), nullable=False)
    modified_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now(), onupdate=datetime.now, nullable=False)

class SecurityUser(UserMixin):

    def __init__(self, username):
        self._username = username

    def get_id(self):
        return self._username


class Service(object):

    def __init__(self, name: str):
        self._name = name
        self._app_token = False
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
        if 'app_token' in config:
            service._app_token = bool(config['app_token'])
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
    def app_token(self) -> bool:
        return self._app_token

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


class User(BaseModel, ModelUpdatedMixin):
    id: Mapped[uuid.UUID] = mapped_column(db.Uuid, primary_key=True, default=uuid.uuid4)
    username: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    password_hashed: Mapped[str] = mapped_column(db.String, nullable=False)
    alternative_email: Mapped[Optional[str]] = mapped_column( db.String, nullable=True)
    last_login: Mapped[Optional[datetime]] = mapped_column(db.DateTime, nullable=True)

    enabled: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)

    app_tokens: Mapped[List['AppToken']] = relationship('AppToken', back_populates='user')
    # totps: Mapped[List['Totp']] = relationship('Totp', back_populates='user', default_factory=list)
    # webauthn_credentials: Mapped[List['WebauthnCredential']] = relationship('WebauthnCredential', back_populates='user', cascade='delete,delete-orphan', passive_deletes=True, default_factory=list)

    @property
    def totps(self) -> List['Totp']:
        return []
    @property
    def webauthn_credentials(self) -> List['WebauthnCredential']:
        return []

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @property
    def is_authenticated(self) -> bool:
        return True  # TODO

    def get(self, key) -> None:
        print(f'getitem: {key}') # TODO

    @property
    def groups(self) -> list['Group']:
        if self.username == 'tuxcoder':
            return [Group(name='admin')]
        else:
            return []

    @property
    def email(self) -> str:
        domain = current_app.config['DOMAIN']
        return f'{self.username}@{domain}'

    def change_password(self, password_new: str) -> None:
        self.password_hashed = crypt.crypt(password_new)

    def get_token_by_name(self, name: str) -> Optional['AppToken']:
        for token in self.app_tokens:
            if token.name == name:
                return token
        return None
        

    def get_token_by_scope(self, scope: str) -> Iterator['AppToken']:
        for token in self.app_tokens:
            if scope in token.scopes.split():
                yield token # type: ignore


class AppToken(BaseModel, ModelUpdatedMixin):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scopes: Mapped[str] = mapped_column(nullable=False) # string of a list seperated by `,` 
    user_id: Mapped[uuid.UUID] = mapped_column(
            db.Uuid,
            db.ForeignKey(User.id), nullable=False)
    user: Mapped[User] = relationship(User, back_populates="app_tokens")
    token: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    last_used: Mapped[Optional[datetime]] = mapped_column(db.DateTime, nullable=True, default=None)

    @staticmethod
    def new(user: User, scopes: str, name: str):
        alphabet = string.ascii_letters + string.digits
        token = ''.join(secrets.choice(alphabet) for i in range(12))
        return AppToken(scopes=scopes, token=token, user=user, name=name)

class Totp(BaseModel, ModelUpdatedMixin):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    secret: Mapped[str] = mapped_column(db.String, nullable=False)
    name: Mapped[str] = mapped_column(db.String, nullable=False)

    user_id: Mapped[uuid.UUID] = mapped_column(
            db.Uuid,
            db.ForeignKey(User.id), nullable=False)
    # user: Mapped[User] = relationship(User, back_populates="totp")
    last_used: Mapped[Optional[datetime]] = mapped_column(db.DateTime, nullable=True, default=None)

    def verify(self, token: str) -> bool:
        totp = pyotp.TOTP(self.secret)
        return totp.verify(token)


class WebauthnCredential(BaseModel, ModelUpdatedMixin):  # pylint: disable=too-few-public-methods
    """Webauthn credential model"""

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[uuid.UUID] = mapped_column(db.Uuid, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user_handle: Mapped[str] = mapped_column(db.String(64), nullable=False)
    credential_data: Mapped[bytes] = mapped_column(db.LargeBinary, nullable=False)
    name: Mapped[str] = mapped_column(db.String(250), nullable=False)
    registered: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow, nullable=False)

    # user = db.relationship('User', back_populates='webauthn_credentials')


class Group(BaseModel, ModelUpdatedMixin):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(), nullable=False, unique=True)

