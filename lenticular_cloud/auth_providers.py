from flask import current_app
from .form.auth import PasswordForm, TotpForm, Fido2Form
from ldap3 import Server, Connection, HASHED_SALTED_SHA256
from ldap3.core.exceptions import LDAPException
from .model import User
import logging


logger = logging.getLogger(__name__)



class AuthProvider:

    @classmethod
    def get_name(csl):
        return csl.__name__

    @staticmethod
    def get_form():
        return

    @staticmethod
    def check_auth(user, form) -> bool:
        '''
        checks the submited form is valid
        return true if user is allowed to auth
        '''
        return False


class LdapAuthProvider(AuthProvider):

    @staticmethod
    def get_form():
        return PasswordForm(prefix='password')

    @staticmethod
    def check_auth(user: User, form):
        return LdapAuthProvider.check_auth_internal(
                user, form.data['password'])

    @staticmethod
    def check_auth_internal(user, password):
        server = Server(current_app.config['LDAP_URL'])
        ldap_conn = Connection(server, user.entry_dn, password)
        try:
            return ldap_conn.bind()
        except LDAPException:
            return False


class U2FAuthProvider(AuthProvider):
    @staticmethod
    def get_from():
        return Fido2Form(prefix='fido2')


class WebAuthProvider(AuthProvider):
    pass


class TotpAuthProvider(AuthProvider):

    @staticmethod
    def get_form():
        return TotpForm(prefix='totp')

    @staticmethod
    def check_auth(user, form):
        data = form.data['totp']
        if data is not None:
            print(f'data totp: {data}')
            if len(user.totps) == 0:  # migration, TODO remove
                return True
            for totp in user.totps:
                if totp.verify(data):
                    return True
        return False


AUTH_PROVIDER_LIST = [
    LdapAuthProvider,
    TotpAuthProvider
]

print(LdapAuthProvider.get_name())

