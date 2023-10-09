from flask import Flask
from ory_hydra_client import Client
from typing import Optional
from ory_hydra_client.api.o_auth_2 import list_o_auth_2_clients, create_o_auth_2_client
from ory_hydra_client.models.o_auth_20_client import OAuth20Client


class HydraService:

    def __init__(self) -> None:
        self._hydra_client: Optional[Client] = None
        self._oauth_client: Optional[Client] = None

        self.client_id = ''
        self.client_secret = ''

    def init_app(self, app: Flask) -> None:

        self.set_hydra_client(Client(base_url=app.config['HYDRA_ADMIN_URL']))

        client_name = app.config['OAUTH_ID']
        client_secret = app.config['OAUTH_SECRET']

        clients = list_o_auth_2_clients.sync_detailed(_client=self.hydra_client).parsed
        if clients is None:
            raise RuntimeError("could not get clients list")
        client: Optional[OAuth20Client] = None
        for c in clients:
            if c.client_name == client_name:
                client = c
                break

        if client is None:
            domain = app.config['DOMAIN']
            client = OAuth20Client(
                client_name="identiy_provider",
                # client_id=client_id,
                client_secret=client_secret,
                response_types=["code", "id_token"],
                scope="openid profile manage",
                grant_types=["authorization_code", "refresh_token"],
                redirect_uris=[ f"https://{domain}/oauth/authorized" ],
                token_endpoint_auth_method="client_secret_basic",
            )
            ret = create_o_auth_2_client.sync(json_body=client, _client=self.hydra_client)
            if ret is None:
                raise RuntimeError("could not crate account")
        if type(client.client_id) is not str:
            raise RuntimeError("could not parse client_id from ory-hydra")
        self.client_id = client.client_id
        self.client_secret = client_secret


    @property
    def hydra_client(self) -> Client:
        if self._hydra_client is None:
            raise RuntimeError('need to init client first')
        return self._hydra_client

    def set_hydra_client(self, client: Client) -> None:
        self._hydra_client = client

    @property
    def oauth_client(self) -> Client:
        if self._oauth_client is None:
            raise RuntimeError('need to init client first')
        return self._oauth_client

    def set_oauth_client(self, client: Client) -> None:
        self._hydra_client = client


hydra_service = HydraService()
