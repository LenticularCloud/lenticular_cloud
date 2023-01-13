from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.is_ready_response_200 import IsReadyResponse200
from ...models.is_ready_response_503 import IsReadyResponse503



def _get_kwargs(
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/health/ready".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[IsReadyResponse200, IsReadyResponse503]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IsReadyResponse200.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = IsReadyResponse503.from_dict(response.json())



        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[IsReadyResponse200, IsReadyResponse503]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[Union[IsReadyResponse200, IsReadyResponse503]]:
    """Check HTTP Server and Database Status

     This endpoint returns a HTTP 200 status code when Ory Hydra is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of Ory Hydra, the health status will never
    refer to the cluster state, only to a single instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IsReadyResponse200, IsReadyResponse503]]
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

) -> Optional[Union[IsReadyResponse200, IsReadyResponse503]]:
    """Check HTTP Server and Database Status

     This endpoint returns a HTTP 200 status code when Ory Hydra is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of Ory Hydra, the health status will never
    refer to the cluster state, only to a single instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IsReadyResponse200, IsReadyResponse503]]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[Union[IsReadyResponse200, IsReadyResponse503]]:
    """Check HTTP Server and Database Status

     This endpoint returns a HTTP 200 status code when Ory Hydra is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of Ory Hydra, the health status will never
    refer to the cluster state, only to a single instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IsReadyResponse200, IsReadyResponse503]]
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

) -> Optional[Union[IsReadyResponse200, IsReadyResponse503]]:
    """Check HTTP Server and Database Status

     This endpoint returns a HTTP 200 status code when Ory Hydra is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of Ory Hydra, the health status will never
    refer to the cluster state, only to a single instance.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[IsReadyResponse200, IsReadyResponse503]]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

