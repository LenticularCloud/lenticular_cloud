from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.logout_request import LogoutRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    logout_challenge: str,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/logout".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["logout_challenge"] = logout_challenge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, LogoutRequest]]:
    if response.status_code == 200:
        response_200 = LogoutRequest.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GenericError.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, LogoutRequest]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    logout_challenge: str,
) -> Response[Union[GenericError, LogoutRequest]]:
    """Get a Logout Request

     Use this endpoint to fetch a logout request.

    Args:
        logout_challenge (str):

    Returns:
        Response[Union[GenericError, LogoutRequest]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        logout_challenge=logout_challenge,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    logout_challenge: str,
) -> Optional[Union[GenericError, LogoutRequest]]:
    """Get a Logout Request

     Use this endpoint to fetch a logout request.

    Args:
        logout_challenge (str):

    Returns:
        Response[Union[GenericError, LogoutRequest]]
    """

    return sync_detailed(
        _client=_client,
        logout_challenge=logout_challenge,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    logout_challenge: str,
) -> Response[Union[GenericError, LogoutRequest]]:
    """Get a Logout Request

     Use this endpoint to fetch a logout request.

    Args:
        logout_challenge (str):

    Returns:
        Response[Union[GenericError, LogoutRequest]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        logout_challenge=logout_challenge,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    logout_challenge: str,
) -> Optional[Union[GenericError, LogoutRequest]]:
    """Get a Logout Request

     Use this endpoint to fetch a logout request.

    Args:
        logout_challenge (str):

    Returns:
        Response[Union[GenericError, LogoutRequest]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            logout_challenge=logout_challenge,
        )
    ).parsed
