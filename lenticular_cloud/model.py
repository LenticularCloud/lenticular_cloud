from flask import current_app
from ldap3_orm import AttrDef, EntryBase as _EntryBase, ObjectDef, EntryType
from ldap3_orm import Reader
from ldap3 import Entry
from ldap3.utils.conv import escape_filter_chars
from flask_login import UserMixin
from ldap3.core.exceptions import LDAPSessionTerminatedByServerError
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from collections.abc import MutableSequence
from datetime import datetime
import pyotp
import json

ldap_conn = None  # type: Connection
base_dn = ''


class SecurityUser(UserMixin):

    def __init__(self, username):
        self._username = username

    def get_id(self):
        return self._username


class LambdaStr:

    def __init__(self, lam):
        self.lam = lam

    def __str__(self):
        return self.lam()


class EntryBase(object):
    _type = None  # will get replaced by the local type
    _query_object = None  # will get replaced by the local type
    _base_dn = LambdaStr(lambda: base_dn)

    def __init__(self, ldap_object=None, **kwargs):
        if ldap_object is None:
            self._ldap_object = self.get_type()(**kwargs)
        else:
            self._ldap_object = ldap_object

    def __str__(self):
        return str(self._ldap_object)

    @classmethod
    def get_object_def(cls):
        return ObjectDef(cls.object_classes, ldap_conn)

    @classmethod
    def get_base(cls):
        return cls.base_dn.format(_base_dn=base_dn)

    @classmethod
    def get_type(cls):
        if cls._type is None:
            cls._type = EntryType(cls.dn.replace('{base_dn}',cls.get_base()), cls.object_classes, ldap_conn)
        return cls._type

    def commit(self):
        print(self._ldap_object.entry_attributes_as_dict)
        ret = ldap_conn.add(
                self.dn, self.object_classes, self._ldap_object.entry_attributes_as_dict)
        print(ret)
        pass

    @classmethod
    def query(cls):
        if cls._query_object is None:
            cls._query_object = cls._query(cls)
        return cls._query_object


    class _query(object):
        def __init__(self, clazz):
            self._class = clazz

        def _query(self, ldap_filter: str):
            reader = Reader(ldap_conn, self._class.get_object_def(), self._class.get_base(), ldap_filter)
            try:
                reader.search()
            except LDAPSessionTerminatedByServerError:
                ldap_conn.bind()
                reader.search()
            return list(reader)

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
            service._pki_config = config['pki_config']

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

    def __init__(self, cn, ca_name, cert_data):
        self._cn = cn
        self._ca_name = ca_name
        self._cert_data = cert_data

    @property
    def cn(self):
        return self._cn

    @property
    def ca_name(self):
        return self._ca_name

    @property
    def not_valid_before(self):
        return self._cert_data.not_valid_before

    @property
    def not_valid_after(self):
        return self._cert_data.not_valid_after

    def fingerprint(self, algorithm=hashes.SHA256()):
        return self._cert_data.fingerprint(algorithm)

    def pem(self):
        return self._cert_data.public_bytes(encoding=serialization.Encoding.PEM).decode()

    def __str__(self):
        return f'Certificate(cn={self._cn}, ca_name={self._ca_name}, not_valid_before={self.not_valid_before}, not_valid_after={self.not_valid_after})'


class Totp(object):

    def __init__(self, name, secret, created_at=datetime.now()):
        self._secret = secret
        self._name = name
        self._created_at = created_at

    @property
    def name(self):
        return self._name

    @property
    def created_at(self):
        return self._created_at

    def verify(self, token: str):
        totp = pyotp.TOTP(self._secret)
        return totp.verify(token)

    def to_dict(self):
        return {
                'secret': self._secret,
                'name': self._name,
                'created_at': int(self._created_at.timestamp())}

    @staticmethod
    def from_dict(data):
        return Totp(
                name=data['name'],
                secret=data['secret'],
                created_at=datetime.fromtimestamp(data['created_at']))


class TotpList(MutableSequence):
    def __init__(self, ldap_attr):
        super().__init__()
        self._ldap_attr = ldap_attr

    def __getitem__(self, ii):
        return Totp.from_dict(json.loads(self._ldap_attr[ii]))

    def __setitem__(self, ii, val: Totp):
        self._ldap_attr[ii] = json.dumps(val.to_dict()).encode()

    def __len__(self):
        return len(self._ldap_attr)

    def __delitem__(self, ii):
        del self._ldap_attr[ii]

    def delete(self, totp_name):
        for i in range(len(self)):
            if self[i].name == totp_name:
                self._ldap_attr.delete(self._ldap_attr[i])

    def insert(self, ii, val):
        self.append(val)

    def append(self, val):
        self._ldap_attr.add(json.dumps(val.to_dict()).encode())


class User(EntryBase):

    dn = "uid={uid},{base_dn}"
    base_dn = "ou=users,{_base_dn}"
    object_classes = ["top", "inetOrgPerson", "LenticularUser"]

    def __init__(self, ldap_object=None, **kwargs):
        super().__init__(ldap_object, **kwargs)
        self._totp_list = TotpList(ldap_object.totpSecret)

    @property
    def is_authenticated(self):
        return True  # TODO

    def get(self, key):
        print(f'getitem: {key}')

    def make_writeable(self):
        self._ldap_object = self._ldap_object.entry_writable()
        self._totp_list = TotpList(self._ldap_object.totpSecret)

    @property
    def entry_dn(self):
        return self._ldap_object.entry_dn

    @property
    def username(self):
        return self._ldap_object.uid

    @username.setter
    def username(self, value):
        self._ldap_object.uid = value

    @property
    def userPassword(self):
        return self._ldap_object.userPassword

    @property
    def fullname(self):
        return self._ldap_object.fullname

    @property
    def givenname(self):
        return self._ldap_object.givenname

    @property
    def surname(self):
        return self._ldap_object.surname

    @property
    def mail(self):
        return self._ldap_object.mail

    @property
    def alternative_email(self):
        return self._ldap_object.altMail

    @property
    def auth_role(self):
        return self._ldap_object.authRole

    @property
    def gpg_public_key(self):
        return self._ldap_object.gpgPublicKey

    @property
    def totps(self):
        return self._totp_list

    class _query(EntryBase._query):
        def by_username(self, username) -> 'User':
            result = self._query('(uid={username:s})'.format(username=escape_filter_chars(username)))
            if len(result) > 0:
                return User(result[0])
            else:
                return None



class Group(EntryBase):
    dn = "cn={cn},{base_dn}"
    base_dn = "ou=Users,{_base_dn}"
    object_classes = ["top"]

    fullname = AttrDef("cn")
