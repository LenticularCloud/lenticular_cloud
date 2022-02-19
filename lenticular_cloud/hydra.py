from ory_hydra_client import Client
from typing import Optional



class HydraService:

    def __init__(self):
        self._hydra_client = None # type: Optional[Client]
        self._oauth_client = None # type: Optional[Client]

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
