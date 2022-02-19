from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/metrics/prometheus".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Any]:
    """Get Snapshot Metrics from the Hydra Service.

     If you're using k8s, you can then add annotations to your deployment like so:

    ```
    metadata:
    annotations:
    prometheus.io/port: \"4445\"
    prometheus.io/path: \"/metrics/prometheus\"
    ```

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Any]:
    """Get Snapshot Metrics from the Hydra Service.

     If you're using k8s, you can then add annotations to your deployment like so:

    ```
    metadata:
    annotations:
    prometheus.io/port: \"4445\"
    prometheus.io/path: \"/metrics/prometheus\"
    ```

    If the service supports TLS Edge Termination, this endpoint does not require the
    `X-Forwarded-Proto` header to be set.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)
