from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.o_auth_20_redirect_browser_to import OAuth20RedirectBrowserTo
from typing import Dict
from ...models.handled_login_request_is_the_request_payload_used_to_accept_a_login_request import HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest
from typing import cast



def _get_kwargs(
    *,
    _client: Client,
    json_body: HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest,
    login_challenge: str,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/requests/login/accept".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["login_challenge"] = login_challenge



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body = json_body.to_dict()



    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OAuth20RedirectBrowserTo]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuth20RedirectBrowserTo.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OAuth20RedirectBrowserTo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    json_body: HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest,
    login_challenge: str,

) -> Response[OAuth20RedirectBrowserTo]:
    """Accept OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    This endpoint tells Ory that the subject has successfully authenticated and includes additional
    information such as
    the subject's ID and if Ory should remember the subject's subject agent for future authentication
    attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20RedirectBrowserTo]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,
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
    json_body: HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest,
    login_challenge: str,

) -> Optional[OAuth20RedirectBrowserTo]:
    """Accept OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    This endpoint tells Ory that the subject has successfully authenticated and includes additional
    information such as
    the subject's ID and if Ory should remember the subject's subject agent for future authentication
    attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20RedirectBrowserTo]
    """


    return sync_detailed(
        _client=_client,
json_body=json_body,
login_challenge=login_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    json_body: HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest,
    login_challenge: str,

) -> Response[OAuth20RedirectBrowserTo]:
    """Accept OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    This endpoint tells Ory that the subject has successfully authenticated and includes additional
    information such as
    the subject's ID and if Ory should remember the subject's subject agent for future authentication
    attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20RedirectBrowserTo]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,
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
    json_body: HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest,
    login_challenge: str,

) -> Optional[OAuth20RedirectBrowserTo]:
    """Accept OAuth 2.0 Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell the Ory OAuth2 Service about it.

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    This endpoint tells Ory that the subject has successfully authenticated and includes additional
    information such as
    the subject's ID and if Ory should remember the subject's subject agent for future authentication
    attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (HandledLoginRequestIsTheRequestPayloadUsedToAcceptALoginRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth20RedirectBrowserTo]
    """


    return (await asyncio_detailed(
        _client=_client,
json_body=json_body,
login_challenge=login_challenge,

    )).parsed

