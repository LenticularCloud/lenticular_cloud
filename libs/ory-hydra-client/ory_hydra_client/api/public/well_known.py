from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.json_web_key_set import JSONWebKeySet
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/.well-known/jwks.json".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, JSONWebKeySet]]:
    if response.status_code == 200:
        response_200 = JSONWebKeySet.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, JSONWebKeySet]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, JSONWebKeySet]]:
    """JSON Web Keys Discovery

     This endpoint returns JSON Web Keys to be used as public keys for verifying OpenID Connect ID Tokens
    and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
) -> Optional[Union[GenericError, JSONWebKeySet]]:
    """JSON Web Keys Discovery

     This endpoint returns JSON Web Keys to be used as public keys for verifying OpenID Connect ID Tokens
    and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, JSONWebKeySet]]:
    """JSON Web Keys Discovery

     This endpoint returns JSON Web Keys to be used as public keys for verifying OpenID Connect ID Tokens
    and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
) -> Optional[Union[GenericError, JSONWebKeySet]]:
    """JSON Web Keys Discovery

     This endpoint returns JSON Web Keys to be used as public keys for verifying OpenID Connect ID Tokens
    and,
    if enabled, OAuth 2.0 JWT Access Tokens. This endpoint can be used with client libraries like
    [node-jwks-rsa](https://github.com/auth0/node-jwks-rsa) among others.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed
