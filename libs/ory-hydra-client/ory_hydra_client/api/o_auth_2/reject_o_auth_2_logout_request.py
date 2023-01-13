from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    *,
    _client: Client,
    logout_challenge: str,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/requests/logout/reject".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["logout_challenge"] = logout_challenge



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
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
    logout_challenge: str,

) -> Response[Any]:
    """Reject OAuth 2.0 Session Logout Request

     When a user or an application requests Ory OAuth 2.0 to remove the session state of a subject, this
    endpoint is used to deny that logout request.
    No HTTP request body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,
logout_challenge=logout_challenge,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


async def asyncio_detailed(
    *,
    _client: Client,
    logout_challenge: str,

) -> Response[Any]:
    """Reject OAuth 2.0 Session Logout Request

     When a user or an application requests Ory OAuth 2.0 to remove the session state of a subject, this
    endpoint is used to deny that logout request.
    No HTTP request body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,
logout_challenge=logout_challenge,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)


