from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.o_auth_20_redirect_browser_to import OAuth20RedirectBrowserTo
from typing import Dict
from ...models.contains_information_about_an_ongoing_logout_request import ContainsInformationAboutAnOngoingLogoutRequest



def _get_kwargs(
    *,
    _client: Client,
    logout_challenge: str,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/requests/logout".format(
        _client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ContainsInformationAboutAnOngoingLogoutRequest.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.GONE:
        response_410 = OAuth20RedirectBrowserTo.from_dict(response.json())



        return response_410
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
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

) -> Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Session Logout Request

     Use this endpoint to fetch an Ory OAuth 2.0 logout request.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]
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

def sync(
    *,
    _client: Client,
    logout_challenge: str,

) -> Optional[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Session Logout Request

     Use this endpoint to fetch an Ory OAuth 2.0 logout request.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]
    """


    return sync_detailed(
        _client=_client,
logout_challenge=logout_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    logout_challenge: str,

) -> Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Session Logout Request

     Use this endpoint to fetch an Ory OAuth 2.0 logout request.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]
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

async def asyncio(
    *,
    _client: Client,
    logout_challenge: str,

) -> Optional[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Session Logout Request

     Use this endpoint to fetch an Ory OAuth 2.0 logout request.

    Args:
        logout_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationAboutAnOngoingLogoutRequest, OAuth20RedirectBrowserTo]]
    """


    return (await asyncio_detailed(
        _client=_client,
logout_challenge=logout_challenge,

    )).parsed

