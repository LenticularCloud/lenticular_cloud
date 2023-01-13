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
    *,
    _client: Client,
    json_body: OAuth20Client,

) -> Dict[str, Any]:
    url = "{}/admin/clients".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, OAuth20Client]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OAuth20Client.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
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
    *,
    _client: Client,
    json_body: OAuth20Client,

) -> Response[Union[Any, OAuth20Client]]:
    """Create OAuth 2.0 Client

     Create a new OAuth 2.0 client. If you pass `client_secret` the secret is used, otherwise a random
    secret
    is generated. The secret is echoed in the response. It is not possible to retrieve it later on.

    Args:
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
        _client=_client,
json_body=json_body,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    json_body: OAuth20Client,

) -> Optional[Union[Any, OAuth20Client]]:
    """Create OAuth 2.0 Client

     Create a new OAuth 2.0 client. If you pass `client_secret` the secret is used, otherwise a random
    secret
    is generated. The secret is echoed in the response. It is not possible to retrieve it later on.

    Args:
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
        _client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    json_body: OAuth20Client,

) -> Response[Union[Any, OAuth20Client]]:
    """Create OAuth 2.0 Client

     Create a new OAuth 2.0 client. If you pass `client_secret` the secret is used, otherwise a random
    secret
    is generated. The secret is echoed in the response. It is not possible to retrieve it later on.

    Args:
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
        _client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    json_body: OAuth20Client,

) -> Optional[Union[Any, OAuth20Client]]:
    """Create OAuth 2.0 Client

     Create a new OAuth 2.0 client. If you pass `client_secret` the secret is used, otherwise a random
    secret
    is generated. The secret is echoed in the response. It is not possible to retrieve it later on.

    Args:
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
        _client=_client,
json_body=json_body,

    )).parsed

