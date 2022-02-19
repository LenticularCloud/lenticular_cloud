from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.o_auth_2_client import OAuth2Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    _client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/clients".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, List[OAuth2Client]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = OAuth2Client.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, List[OAuth2Client]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[GenericError, List[OAuth2Client]]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets. As a default it
    lists the first 100 clients. The `limit` parameter can be used to retrieve more clients, but it has
    an upper bound at 500 objects. Pagination should be used to retrieve more than 500 objects.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.
    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-url/admin/clients?limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[GenericError, List[OAuth2Client]]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[GenericError, List[OAuth2Client]]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets. As a default it
    lists the first 100 clients. The `limit` parameter can be used to retrieve more clients, but it has
    an upper bound at 500 objects. Pagination should be used to retrieve more than 500 objects.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.
    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-url/admin/clients?limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[GenericError, List[OAuth2Client]]]
    """

    return sync_detailed(
        _client=_client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[GenericError, List[OAuth2Client]]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets. As a default it
    lists the first 100 clients. The `limit` parameter can be used to retrieve more clients, but it has
    an upper bound at 500 objects. Pagination should be used to retrieve more than 500 objects.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.
    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-url/admin/clients?limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[GenericError, List[OAuth2Client]]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[GenericError, List[OAuth2Client]]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets. As a default it
    lists the first 100 clients. The `limit` parameter can be used to retrieve more clients, but it has
    an upper bound at 500 objects. Pagination should be used to retrieve more than 500 objects.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.
    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-url/admin/clients?limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):

    Returns:
        Response[Union[GenericError, List[OAuth2Client]]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            limit=limit,
            offset=offset,
        )
    ).parsed
