from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.health_status import HealthStatus
from typing import cast
from ...models.health_not_ready_status import HealthNotReadyStatus
from typing import Dict



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


def _parse_response(*, response: httpx.Response) -> Optional[Union[HealthNotReadyStatus, HealthStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = HealthStatus.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = HealthNotReadyStatus.from_dict(response.json())



        return response_503
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[HealthNotReadyStatus, HealthStatus]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[Union[HealthNotReadyStatus, HealthStatus]]:
    """Check Readiness Status

     This endpoint returns a 200 status code when the HTTP server is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of this service, the health status will never
    refer to the cluster state, only to a single instance.

    Returns:
        Response[Union[HealthNotReadyStatus, HealthStatus]]
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

) -> Optional[Union[HealthNotReadyStatus, HealthStatus]]:
    """Check Readiness Status

     This endpoint returns a 200 status code when the HTTP server is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of this service, the health status will never
    refer to the cluster state, only to a single instance.

    Returns:
        Response[Union[HealthNotReadyStatus, HealthStatus]]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[Union[HealthNotReadyStatus, HealthStatus]]:
    """Check Readiness Status

     This endpoint returns a 200 status code when the HTTP server is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of this service, the health status will never
    refer to the cluster state, only to a single instance.

    Returns:
        Response[Union[HealthNotReadyStatus, HealthStatus]]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,

) -> Optional[Union[HealthNotReadyStatus, HealthStatus]]:
    """Check Readiness Status

     This endpoint returns a 200 status code when the HTTP server is up running and the environment
    dependencies (e.g.
    the database) are responsive as well.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Be aware that if you are running multiple nodes of this service, the health status will never
    refer to the cluster state, only to a single instance.

    Returns:
        Response[Union[HealthNotReadyStatus, HealthStatus]]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

