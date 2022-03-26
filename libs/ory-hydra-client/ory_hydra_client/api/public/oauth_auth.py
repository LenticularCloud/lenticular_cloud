from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GenericError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Union[Any, GenericError]]:
    """The OAuth 2.0 Authorize Endpoint

     This endpoint is not documented here because you should never use your own implementation to perform
    OAuth2 flows.
    OAuth2 is a very popular protocol and a library for your programming language will exists.

    To learn more about this flow please refer to the specification: https://tools.ietf.org/html/rfc6749

    Returns:
        Response[Union[Any, GenericError]]
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
) -> Optional[Union[Any, GenericError]]:
    """The OAuth 2.0 Authorize Endpoint

     This endpoint is not documented here because you should never use your own implementation to perform
    OAuth2 flows.
    OAuth2 is a very popular protocol and a library for your programming language will exists.

    To learn more about this flow please refer to the specification: https://tools.ietf.org/html/rfc6749

    Returns:
        Response[Union[Any, GenericError]]
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Union[Any, GenericError]]:
    """The OAuth 2.0 Authorize Endpoint

     This endpoint is not documented here because you should never use your own implementation to perform
    OAuth2 flows.
    OAuth2 is a very popular protocol and a library for your programming language will exists.

    To learn more about this flow please refer to the specification: https://tools.ietf.org/html/rfc6749

    Returns:
        Response[Union[Any, GenericError]]
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
) -> Optional[Union[Any, GenericError]]:
    """The OAuth 2.0 Authorize Endpoint

     This endpoint is not documented here because you should never use your own implementation to perform
    OAuth2 flows.
    OAuth2 is a very popular protocol and a library for your programming language will exists.

    To learn more about this flow please refer to the specification: https://tools.ietf.org/html/rfc6749

    Returns:
        Response[Union[Any, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed