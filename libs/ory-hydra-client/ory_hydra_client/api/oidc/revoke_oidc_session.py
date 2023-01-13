from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/oauth2/sessions/logout".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.FOUND:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[Any]:
    """OpenID Connect Front- and Back-channel Enabled Logout

     This endpoint initiates and completes user logout at the Ory OAuth2 & OpenID provider and initiates
    OpenID Connect Front- / Back-channel logout:

    https://openid.net/specs/openid-connect-frontchannel-1_0.html
    https://openid.net/specs/openid-connect-backchannel-1_0.html

    Back-channel logout is performed asynchronously and does not affect logout flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

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

    return _build_response(client=_client, response=response)


async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[Any]:
    """OpenID Connect Front- and Back-channel Enabled Logout

     This endpoint initiates and completes user logout at the Ory OAuth2 & OpenID provider and initiates
    OpenID Connect Front- / Back-channel logout:

    https://openid.net/specs/openid-connect-frontchannel-1_0.html
    https://openid.net/specs/openid-connect-backchannel-1_0.html

    Back-channel logout is performed asynchronously and does not affect logout flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)


