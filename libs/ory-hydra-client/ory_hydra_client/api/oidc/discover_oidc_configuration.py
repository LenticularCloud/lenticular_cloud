from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.open_id_connect_discovery_metadata import OpenIDConnectDiscoveryMetadata
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/.well-known/openid-configuration".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OpenIDConnectDiscoveryMetadata]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OpenIDConnectDiscoveryMetadata.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OpenIDConnectDiscoveryMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[OpenIDConnectDiscoveryMetadata]:
    """OpenID Connect Discovery

     A mechanism for an OpenID Connect Relying Party to discover the End-User's OpenID Provider and
    obtain information needed to interact with it, including its OAuth 2.0 endpoint locations.

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenIDConnectDiscoveryMetadata]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,

) -> Optional[OpenIDConnectDiscoveryMetadata]:
    """OpenID Connect Discovery

     A mechanism for an OpenID Connect Relying Party to discover the End-User's OpenID Provider and
    obtain information needed to interact with it, including its OAuth 2.0 endpoint locations.

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenIDConnectDiscoveryMetadata]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[OpenIDConnectDiscoveryMetadata]:
    """OpenID Connect Discovery

     A mechanism for an OpenID Connect Relying Party to discover the End-User's OpenID Provider and
    obtain information needed to interact with it, including its OAuth 2.0 endpoint locations.

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenIDConnectDiscoveryMetadata]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,

) -> Optional[OpenIDConnectDiscoveryMetadata]:
    """OpenID Connect Discovery

     A mechanism for an OpenID Connect Relying Party to discover the End-User's OpenID Provider and
    obtain information needed to interact with it, including its OAuth 2.0 endpoint locations.

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpenIDConnectDiscoveryMetadata]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

