from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.version import Version
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/version".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Version]:
    if response.status_code == 200:
        response_200 = Version.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Version]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Version]:
    """Get Service Version

     This endpoint returns the service version typically notated using semantic versioning.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Version]
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
) -> Optional[Version]:
    """Get Service Version

     This endpoint returns the service version typically notated using semantic versioning.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Version]
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Version]:
    """Get Service Version

     This endpoint returns the service version typically notated using semantic versioning.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Version]
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
) -> Optional[Version]:
    """Get Service Version

     This endpoint returns the service version typically notated using semantic versioning.

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Version]
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed
