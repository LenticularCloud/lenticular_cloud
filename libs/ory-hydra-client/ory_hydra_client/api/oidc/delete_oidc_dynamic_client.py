from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    id: str,
    *,
    _client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/oauth2/register/{id}".format(
        _client.base_url,id=id)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    _client: AuthenticatedClient,

) -> Response[Any]:
    """Delete OAuth 2.0 Client using the OpenID Dynamic Client Registration Management Protocol

     This endpoint behaves like the administrative counterpart (`deleteOAuth2Client`) but is capable of
    facing the
    public internet directly and can be used in self-service. It implements the OpenID Connect
    Dynamic Client Registration Protocol. This feature needs to be enabled in the configuration. This
    endpoint
    is disabled by default. It can be enabled by an administrator.

    To use this endpoint, you will need to present the client's authentication credentials. If the
    OAuth2 Client
    uses the Token Endpoint Authentication Method `client_secret_post`, you need to present the client
    secret in the URL query.
    If it uses `client_secret_basic`, present the Client ID and the Client Secret in the Authorization
    header.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    _client: AuthenticatedClient,

) -> Response[Any]:
    """Delete OAuth 2.0 Client using the OpenID Dynamic Client Registration Management Protocol

     This endpoint behaves like the administrative counterpart (`deleteOAuth2Client`) but is capable of
    facing the
    public internet directly and can be used in self-service. It implements the OpenID Connect
    Dynamic Client Registration Protocol. This feature needs to be enabled in the configuration. This
    endpoint
    is disabled by default. It can be enabled by an administrator.

    To use this endpoint, you will need to present the client's authentication credentials. If the
    OAuth2 Client
    uses the Token Endpoint Authentication Method `client_secret_post`, you need to present the client
    secret in the URL query.
    If it uses `client_secret_basic`, present the Client ID and the Client Secret in the Authorization
    header.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)


