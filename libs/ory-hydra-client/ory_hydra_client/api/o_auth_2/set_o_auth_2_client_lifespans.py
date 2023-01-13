from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.o_auth_20_client_token_lifespans import OAuth20ClientTokenLifespans
from typing import cast
from ...models.o_auth_20_client import OAuth20Client



def _get_kwargs(
    id: str,
    *,
    _client: Client,
    json_body: OAuth20ClientTokenLifespans,

) -> Dict[str, Any]:
    url = "{}/admin/clients/{id}/lifespans".format(
        _client.base_url,id=id)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OAuth20Client]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuth20Client.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OAuth20Client]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    _client: Client,
    json_body: OAuth20ClientTokenLifespans,

) -> Response[OAuth20Client]:
    """Set OAuth2 Client Token Lifespans

     Set lifespans of different token types issued for this OAuth 2.0 client. Does not modify other
    fields.

    Args:
        id (str):
        json_body (OAuth20ClientTokenLifespans): Lifespans of different token types issued for
            this OAuth 2.0 Client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20Client]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,
json_body=json_body,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    id: str,
    *,
    _client: Client,
    json_body: OAuth20ClientTokenLifespans,

) -> Optional[OAuth20Client]:
    """Set OAuth2 Client Token Lifespans

     Set lifespans of different token types issued for this OAuth 2.0 client. Does not modify other
    fields.

    Args:
        id (str):
        json_body (OAuth20ClientTokenLifespans): Lifespans of different token types issued for
            this OAuth 2.0 Client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20Client]
    """


    return sync_detailed(
        id=id,
_client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    _client: Client,
    json_body: OAuth20ClientTokenLifespans,

) -> Response[OAuth20Client]:
    """Set OAuth2 Client Token Lifespans

     Set lifespans of different token types issued for this OAuth 2.0 client. Does not modify other
    fields.

    Args:
        id (str):
        json_body (OAuth20ClientTokenLifespans): Lifespans of different token types issued for
            this OAuth 2.0 Client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20Client]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    id: str,
    *,
    _client: Client,
    json_body: OAuth20ClientTokenLifespans,

) -> Optional[OAuth20Client]:
    """Set OAuth2 Client Token Lifespans

     Set lifespans of different token types issued for this OAuth 2.0 client. Does not modify other
    fields.

    Args:
        id (str):
        json_body (OAuth20ClientTokenLifespans): Lifespans of different token types issued for
            this OAuth 2.0 Client.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20Client]
    """


    return (await asyncio_detailed(
        id=id,
_client=_client,
json_body=json_body,

    )).parsed

