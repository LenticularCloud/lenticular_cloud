from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.oidc_user_info import OidcUserInfo
from typing import Dict
from typing import cast



def _get_kwargs(
    *,
    _client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/userinfo".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OidcUserInfo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OidcUserInfo.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OidcUserInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[OidcUserInfo]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including `session.id_token` values, of
    the provided OAuth 2.0 Access Token's consent request.

    In the case of authentication error, a WWW-Authenticate header might be set in the response
    with more information about the error. See [the
    spec](https://datatracker.ietf.org/doc/html/rfc6750#section-3)
    for more details about header format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcUserInfo]
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
    _client: AuthenticatedClient,

) -> Optional[OidcUserInfo]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including `session.id_token` values, of
    the provided OAuth 2.0 Access Token's consent request.

    In the case of authentication error, a WWW-Authenticate header might be set in the response
    with more information about the error. See [the
    spec](https://datatracker.ietf.org/doc/html/rfc6750#section-3)
    for more details about header format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcUserInfo]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[OidcUserInfo]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including `session.id_token` values, of
    the provided OAuth 2.0 Access Token's consent request.

    In the case of authentication error, a WWW-Authenticate header might be set in the response
    with more information about the error. See [the
    spec](https://datatracker.ietf.org/doc/html/rfc6750#section-3)
    for more details about header format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcUserInfo]
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
    _client: AuthenticatedClient,

) -> Optional[OidcUserInfo]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including `session.id_token` values, of
    the provided OAuth 2.0 Access Token's consent request.

    In the case of authentication error, a WWW-Authenticate header might be set in the response
    with more information about the error. See [the
    spec](https://datatracker.ietf.org/doc/html/rfc6750#section-3)
    for more details about header format.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OidcUserInfo]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

