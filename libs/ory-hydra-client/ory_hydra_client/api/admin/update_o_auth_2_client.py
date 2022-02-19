from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.o_auth_2_client import OAuth2Client
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    _client: Client,
    json_body: OAuth2Client,
) -> Dict[str, Any]:
    url = "{}/clients/{id}".format(_client.base_url, id=id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, OAuth2Client]]:
    if response.status_code == 200:
        response_200 = OAuth2Client.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, OAuth2Client]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    _client: Client,
    json_body: OAuth2Client,
) -> Response[Union[GenericError, OAuth2Client]]:
    """Update an OAuth 2.0 Client

     Update an existing OAuth 2.0 Client. If you pass `client_secret` the secret will be updated and
    returned via the API. This is the only time you will be able to retrieve the client secret, so write
    it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
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

    return _build_response(response=response)


def sync(
    id: str,
    *,
    _client: Client,
    json_body: OAuth2Client,
) -> Optional[Union[GenericError, OAuth2Client]]:
    """Update an OAuth 2.0 Client

     Update an existing OAuth 2.0 Client. If you pass `client_secret` the secret will be updated and
    returned via the API. This is the only time you will be able to retrieve the client secret, so write
    it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
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
    json_body: OAuth2Client,
) -> Response[Union[GenericError, OAuth2Client]]:
    """Update an OAuth 2.0 Client

     Update an existing OAuth 2.0 Client. If you pass `client_secret` the secret will be updated and
    returned via the API. This is the only time you will be able to retrieve the client secret, so write
    it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
    """

    kwargs = _get_kwargs(
        id=id,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    _client: Client,
    json_body: OAuth2Client,
) -> Optional[Union[GenericError, OAuth2Client]]:
    """Update an OAuth 2.0 Client

     Update an existing OAuth 2.0 Client. If you pass `client_secret` the secret will be updated and
    returned via the API. This is the only time you will be able to retrieve the client secret, so write
    it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
    """

    return (
        await asyncio_detailed(
            id=id,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
