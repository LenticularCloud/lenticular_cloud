from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.contains_information_on_an_ongoing_login_request import ContainsInformationOnAnOngoingLoginRequest
from ...models.o_auth_20_redirect_browser_to import OAuth20RedirectBrowserTo
from typing import Dict
from typing import cast



def _get_kwargs(
    *,
    _client: Client,
    login_challenge: str,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/requests/login".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["login_challenge"] = login_challenge



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ContainsInformationOnAnOngoingLoginRequest.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.GONE:
        response_410 = OAuth20RedirectBrowserTo.from_dict(response.json())



        return response_410
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    login_challenge: str,

) -> Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    Per default, the login provider is Ory itself. You may use a different login provider which needs to
    be a web-app
    you write and host, and it must be able to authenticate (\"show the subject a login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]
    """


    kwargs = _get_kwargs(
        _client=_client,
login_challenge=login_challenge,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    login_challenge: str,

) -> Optional[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    Per default, the login provider is Ory itself. You may use a different login provider which needs to
    be a web-app
    you write and host, and it must be able to authenticate (\"show the subject a login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]
    """


    return sync_detailed(
        _client=_client,
login_challenge=login_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    login_challenge: str,

) -> Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    Per default, the login provider is Ory itself. You may use a different login provider which needs to
    be a web-app
    you write and host, and it must be able to authenticate (\"show the subject a login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]
    """


    kwargs = _get_kwargs(
        _client=_client,
login_challenge=login_challenge,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    login_challenge: str,

) -> Optional[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    Per default, the login provider is Ory itself. You may use a different login provider which needs to
    be a web-app
    you write and host, and it must be able to authenticate (\"show the subject a login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingLoginRequest, OAuth20RedirectBrowserTo]]
    """


    return (await asyncio_detailed(
        _client=_client,
login_challenge=login_challenge,

    )).parsed

