from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.json_web_key_set import JsonWebKeySet



def _get_kwargs(
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/.well-known/jwks.json".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[JsonWebKeySet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JsonWebKeySet.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[JsonWebKeySet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[JsonWebKeySet]:
    """Discover Well-Known JSON Web Keys

     This endpoint returns JSON Web Keys required to verifying OpenID Connect ID Tokens and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
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

) -> Optional[JsonWebKeySet]:
    """Discover Well-Known JSON Web Keys

     This endpoint returns JSON Web Keys required to verifying OpenID Connect ID Tokens and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[JsonWebKeySet]:
    """Discover Well-Known JSON Web Keys

     This endpoint returns JSON Web Keys required to verifying OpenID Connect ID Tokens and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
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

) -> Optional[JsonWebKeySet]:
    """Discover Well-Known JSON Web Keys

     This endpoint returns JSON Web Keys required to verifying OpenID Connect ID Tokens and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

