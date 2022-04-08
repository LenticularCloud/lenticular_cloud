# This file is part of sner4 project governed by MIT license, see the LICENSE.txt file.
# source: https://github.com/bodik/flask-webauthn-example/blob/master/fwe/wrapped_fido2_server.py
"""
yubico fido2 server wrapped for flask factory pattern delayed configuration
"""

from socket import getfqdn

from fido2.server import Fido2Server, PublicKeyCredentialRpEntity


class WrappedFido2Server(Fido2Server):
    """yubico fido2 server wrapped for flask factory pattern delayed configuration"""

    def __init__(self):
        """initialize with default rp name"""
        super().__init__(PublicKeyCredentialRpEntity(getfqdn(), 'name'))

    def init_app(self, app) -> None:
        """reinitialize on factory pattern config request"""
        super().__init__(PublicKeyCredentialRpEntity(app.config['SERVER_NAME'] or getfqdn(), 'name'))
