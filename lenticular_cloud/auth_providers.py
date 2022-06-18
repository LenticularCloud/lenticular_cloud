from flask import current_app
from flask_wtf import FlaskForm
from .form.auth import PasswordForm, TotpForm, Fido2Form
from hmac import compare_digest as compare_hash
import crypt
from .model import User
import logging


logger = logging.getLogger(__name__)



class AuthProvider:

    @classmethod
    def get_name(csl):
        return csl.__name__

    @staticmethod
    def get_form() -> FlaskForm:
        return

    @staticmethod
    def check_auth(user: User, form) -> bool:
        '''
        checks the submited form is valid
        return true if user is allowed to auth
        '''
        return False


class PasswordAuthProvider(AuthProvider):

    @staticmethod
    def get_form() -> FlaskForm:
        return PasswordForm(prefix='password')

    @staticmethod
    def check_auth(user: User, form: FlaskForm) -> bool:
        if isinstance(form.data['password'], str):
            return PasswordAuthProvider.check_auth_internal(user, form.data['password'])
        else:
            return False
    @staticmethod
    def check_auth_internal(user: User, password: str) -> bool:
        return compare_hash(crypt.crypt(password, user.password_hashed),user.password_hashed) 


class U2FAuthProvider(AuthProvider):
    @staticmethod
    def get_from() -> FlaskForm:
        return Fido2Form(prefix='fido2')


class WebAuthProvider(AuthProvider):
    pass


class TotpAuthProvider(AuthProvider):

    @staticmethod
    def get_form():
        return TotpForm(prefix='totp')

    @staticmethod
    def check_auth(user: User, form: FlaskForm) -> bool:
        data = form.data['totp']
        if data is not None:
            #print(f'data totp: {data}')
            if len(user.totps) == 0:  # migration, TODO remove
                return True
            for totp in user.totps:
                if totp.verify(data):
                    return True
        return False


AUTH_PROVIDER_LIST = [
    PasswordAuthProvider,
    TotpAuthProvider
]

#print(LdapAuthProvider.get_name())

