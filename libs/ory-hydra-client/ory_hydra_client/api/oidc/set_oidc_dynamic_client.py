from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from typing import cast
from ...models.o_auth_20_client import OAuth20Client



def _get_kwargs(
    id: str,
    *,
    _client: AuthenticatedClient,
    json_body: OAuth20Client,

) -> Dict[str, Any]:
    url = "{}/oauth2/register/{id}".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, OAuth20Client]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuth20Client.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, OAuth20Client]]:
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
    json_body: OAuth20Client,

) -> Response[Union[Any, OAuth20Client]]:
    """Set OAuth2 Client using OpenID Dynamic Client Registration

     This endpoint behaves like the administrative counterpart (`setOAuth2Client`) but is capable of
    facing the
    public internet directly to be used by third parties. It implements the OpenID Connect
    Dynamic Client Registration Protocol.

    This feature is disabled per default. It can be enabled by a system administrator.

    If you pass `client_secret` the secret is used, otherwise the existing secret is used. If set, the
    secret is echoed in the response.
    It is not possible to retrieve it later on.

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
        json_body (OAuth20Client): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID
            Connect flows. Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect
            capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
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
    _client: AuthenticatedClient,
    json_body: OAuth20Client,

) -> Optional[Union[Any, OAuth20Client]]:
    """Set OAuth2 Client using OpenID Dynamic Client Registration

     This endpoint behaves like the administrative counterpart (`setOAuth2Client`) but is capable of
    facing the
    public internet directly to be used by third parties. It implements the OpenID Connect
    Dynamic Client Registration Protocol.

    This feature is disabled per default. It can be enabled by a system administrator.

    If you pass `client_secret` the secret is used, otherwise the existing secret is used. If set, the
    secret is echoed in the response.
    It is not possible to retrieve it later on.

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
        json_body (OAuth20Client): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID
            Connect flows. Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect
            capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    return sync_detailed(
        id=id,
_client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    _client: AuthenticatedClient,
    json_body: OAuth20Client,

) -> Response[Union[Any, OAuth20Client]]:
    """Set OAuth2 Client using OpenID Dynamic Client Registration

     This endpoint behaves like the administrative counterpart (`setOAuth2Client`) but is capable of
    facing the
    public internet directly to be used by third parties. It implements the OpenID Connect
    Dynamic Client Registration Protocol.

    This feature is disabled per default. It can be enabled by a system administrator.

    If you pass `client_secret` the secret is used, otherwise the existing secret is used. If set, the
    secret is echoed in the response.
    It is not possible to retrieve it later on.

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
        json_body (OAuth20Client): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID
            Connect flows. Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect
            capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
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
    _client: AuthenticatedClient,
    json_body: OAuth20Client,

) -> Optional[Union[Any, OAuth20Client]]:
    """Set OAuth2 Client using OpenID Dynamic Client Registration

     This endpoint behaves like the administrative counterpart (`setOAuth2Client`) but is capable of
    facing the
    public internet directly to be used by third parties. It implements the OpenID Connect
    Dynamic Client Registration Protocol.

    This feature is disabled per default. It can be enabled by a system administrator.

    If you pass `client_secret` the secret is used, otherwise the existing secret is used. If set, the
    secret is echoed in the response.
    It is not possible to retrieve it later on.

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
        json_body (OAuth20Client): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID
            Connect flows. Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect
            capabilities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    return (await asyncio_detailed(
        id=id,
_client=_client,
json_body=json_body,

    )).parsed

