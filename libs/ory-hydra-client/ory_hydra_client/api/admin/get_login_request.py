from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.login_request import LoginRequest
from ...models.generic_error import GenericError
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,
    login_challenge: str,

) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/login".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, LoginRequest]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LoginRequest.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GenericError.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GenericError.from_dict(response.json())



        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = GenericError.from_dict(response.json())



        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, LoginRequest]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    login_challenge: str,

) -> Response[Union[GenericError, LoginRequest]]:
    """Get a Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    (sometimes called \"identity provider\") to authenticate the subject and then tell ORY Hydra now
    about it. The login
    provider is an web-app you write and host, and it must be able to authenticate (\"show the subject a
    login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Returns:
        Response[Union[GenericError, LoginRequest]]
    """


    kwargs = _get_kwargs(
        _client=_client,
login_challenge=login_challenge,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    _client: Client,
    login_challenge: str,

) -> Optional[Union[GenericError, LoginRequest]]:
    """Get a Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    (sometimes called \"identity provider\") to authenticate the subject and then tell ORY Hydra now
    about it. The login
    provider is an web-app you write and host, and it must be able to authenticate (\"show the subject a
    login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Returns:
        Response[Union[GenericError, LoginRequest]]
    """


    return sync_detailed(
        _client=_client,
login_challenge=login_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    login_challenge: str,

) -> Response[Union[GenericError, LoginRequest]]:
    """Get a Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    (sometimes called \"identity provider\") to authenticate the subject and then tell ORY Hydra now
    about it. The login
    provider is an web-app you write and host, and it must be able to authenticate (\"show the subject a
    login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Returns:
        Response[Union[GenericError, LoginRequest]]
    """


    kwargs = _get_kwargs(
        _client=_client,
login_challenge=login_challenge,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,
    login_challenge: str,

) -> Optional[Union[GenericError, LoginRequest]]:
    """Get a Login Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    (sometimes called \"identity provider\") to authenticate the subject and then tell ORY Hydra now
    about it. The login
    provider is an web-app you write and host, and it must be able to authenticate (\"show the subject a
    login screen\")
    a subject (in OAuth2 the proper name for subject is \"resource owner\").

    The authentication challenge is appended to the login provider URL to which the subject's user-agent
    (browser) is redirected to. The login
    provider uses that challenge to fetch information on the OAuth2 request and then accept or reject
    the requested authentication process.

    Args:
        login_challenge (str):

    Returns:
        Response[Union[GenericError, LoginRequest]]
    """


    return (await asyncio_detailed(
        _client=_client,
login_challenge=login_challenge,

    )).parsed

