from flask import current_app
from ldap3_orm import AttrDef, EntryBase as _EntryBase, ObjectDef, EntryType
from ldap3_orm import Reader
from ldap3 import Connection, Entry, HASHED_SALTED_SHA256
from ldap3.utils.conv import escape_filter_chars
from ldap3.utils.hashed import hashed
from flask_login import UserMixin
from ldap3.core.exceptions import LDAPSessionTerminatedByServerError
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


logger = logging.getLogger(__name__)
ldap_conn = None  # type: Connection
base_dn = ''

db = SQLAlchemy()  # type: SQLAlchemy
migrate = Migrate()

class UserSignUp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    alternative_email = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.now)


class SecurityUser(UserMixin):

    def __init__(self, username):
        self._username = username

    def get_id(self):
        return self._username


class LambdaStr:

    def __init__(self, lam: Callable[[],str]):
        self.lam = lam

    def __str__(self) -> str:
        return self.lam()


class EntryBase(db.Model):
    __abstract__ = True # for sqlalchemy

    _type = None  # will get replaced by the local type
    _ldap_query_object = None  # will get replaced by the local type
    _base_dn = LambdaStr(lambda: base_dn)

#   def __init__(self, ldap_object=None, **kwargs):
#       if ldap_object is None:
#           self._ldap_object = self.get_type()(**kwargs)
#       else:
#           self._ldap_object = ldap_object
    dn = ''
    base_dn = ''

    def __str__(self) -> str:
        return str(self._ldap_object)

    @classmethod
    def get_object_def(cls) -> ObjectDef:
        return ObjectDef(cls.object_classes, ldap_conn)

    @classmethod
    def get_entry_type(cls) -> EntryType:
        return EntryType(cls.get_dn(), cls.object_classes, ldap_conn)

    @classmethod
    def get_base(cls) -> str:
        return cls.base_dn.format(_base_dn=base_dn)

    @classmethod
    def get_dn(cls) -> str:
        return cls.dn.replace('{base_dn}', cls.get_base())

    @classmethod
    def get_type(cls):
        if cls._type is None:
            cls._type = EntryType(cls.get_dn(), cls.object_classes, ldap_conn)
        return cls._type

    def ldap_commit(self):
        self._ldap_object.entry_commit_changes()

    def ldap_add(self):
        ret = ldap_conn.add(
                self.entry_dn, self.object_classes, self._ldap_object.entry_attributes_as_dict)
        if not ret:
            raise Exception('ldap error')

    @classmethod
    def query_(cls):
        if cls._ldap_query_object is None:
            cls._ldap_query_object = cls._query(cls)
        return cls._ldap_query_object

    class _query(object):
        def __init__(self, clazz):
            self._class = clazz

        def _mapping(self, ldap_object):
            return ldap_object

        def _query(self, ldap_filter: str):
            reader = Reader(ldap_conn, self._class.get_object_def(), self._class.get_base(), ldap_filter)
            try:
                reader.search()
            except LDAPSessionTerminatedByServerError:
                ldap_conn.bind()
                reader.search()
            return [self._mapping(entry) for entry in reader]

        def all(self):
            return self._query(None)


class Service(object):

    def __init__(self, name):
        self._name = name
        self._client_cert = False
        self._pki_config = {
                    'cn': '{username}',
                    'email': '{username}@{domain}'
                }

    @staticmethod
    def from_config(name, config):
        """
        """
        service = Service(name)
        if 'client_cert' in config:
            service._client_cert = bool(config['client_cert'])
        if 'pki_config' in config:
            service._pki_config.update(config['pki_config'])

        return service

    @property
    def name(self):
        return self._name

    @property
    def client_cert(self):
        return self._client_cert

    @property
    def pki_config(self):
        if not self._client_cert:
            raise Exception('invalid call')
        return self._pki_config


class Certificate(object):

    def __init__(self, cn, ca_name: str, cert_data, revoked=False):
        self._cn = cn
        self._ca_name = ca_name
        self._cert_data = cert_data
        self._revoked = revoked
        self._cert_data.not_valid_after.replace(tzinfo=tz.tzutc())
        self._cert_data.not_valid_before.replace(tzinfo=tz.tzutc())

    @property
    def cn(self):
        return self._cn

    @property
    def ca_name(self):
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


class User(EntryBase):
    id = db.Column(
            db.String(length=36), primary_key=True, default=generate_uuid)
    username = db.Column(
            db.String, unique=True, nullable=False)
    alternative_email = db.Column(
            db.String, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now)
    modified_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.now, onupdate=datetime.now)
    last_login = db.Column(db.DateTime, nullable=True)

    totps = db.relationship('Totp', back_populates='user')
    webauthn_credentials = db.relationship('WebauthnCredential', back_populates='user', cascade='delete,delete-orphan', passive_deletes=True)

    dn = "uid={uid},{base_dn}"
    base_dn = "ou=users,{_base_dn}"
    object_classes = ["inetOrgPerson"] #, "LenticularUser"]

    def __init__(self, **kwargs):
        self._ldap_object = None
        super(db.Model).__init__(**kwargs)

    @property
    def is_authenticated(self):
        return True  # TODO

    def get(self, key):
        print(f'getitem: {key}') # TODO

    def make_writeable(self):
        self._ldap_object = self._ldap_object.entry_writable()

    @property
    def groups(self) -> list[str]:
        if self.username == 'tuxcoder':
            return [Group(name='admin')]
        else:
            return []

    @property
    def entry_dn(self) -> str:
        return self._ldap_object.entry_dn

    @property
    def email(self) -> str:
        domain = current_app.config['DOMAIN']
        return f'{self.username}@{domain}'
        return self._ldap_object.mail

    def change_password(self, password_new: str) -> bool:
        self.make_writeable()
        password_hashed = crypt.crypt(password_new)
        self._ldap_object.userPassword = ('{CRYPT}' + password_hashed).encode()
        self.ldap_commit()
        return True

    class _query(EntryBase._query):

        def _mapping(self, ldap_object):
            user = User.query.filter(User.username == str(ldap_object.uid)).first()
            if user is None:
                # migration time
                user = User()
                user.username = str(ldap_object.uid)
                db.session.add(user)
                db.session.commit()
            user._ldap_object = ldap_object
            return user

        def by_username(self, username) -> Optional['User']:
            result = self._query('(uid={username:s})'.format(username=escape_filter_chars(username)))
            if len(result) > 0 and isinstance(result[0], User):
                return result[0]
            else:
                return None

    @staticmethod
    def new(user_data: UserSignUp):
        user = User()
        user.username = user_data.username.lower()
        domain = current_app.config['DOMAIN']
        ldap_object = User.get_entry_type()(
                uid=user_data.username.lower(),
                sn=user_data.username,
                cn=user_data.username,
                userPassword='{CRYPT}' + user_data.password,
                mail=f'{user_data.username}@{domain}')
        user._ldap_object = ldap_object
        user.ldap_add()
        return user



class Totp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    secret = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)

    user_id = db.Column(
            db.String(length=36),
            db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

    def verify(self, token: str):
        totp = pyotp.TOTP(self.secret)
        return totp.verify(token)


class WebauthnCredential(db.Model):  # pylint: disable=too-few-public-methods
    """Webauthn credential model"""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(length=36), db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user_handle = db.Column(db.String(64), nullable=False)
    credential_data = db.Column(db.LargeBinary, nullable=False)
    name = db.Column(db.String(250))
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='webauthn_credentials')


class Group(EntryBase):
    __abstract__ = True # for sqlalchemy, disable for now
    dn = "cn={cn},{base_dn}"
    base_dn = "ou=Users,{_base_dn}"
    object_classes = ["top"]

    fullname = AttrDef("cn")

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)

