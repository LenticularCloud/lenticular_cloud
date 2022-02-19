from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.accept_login_request import AcceptLoginRequest
from ...models.completed_request import CompletedRequest
from ...models.generic_error import GenericError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    json_body: AcceptLoginRequest,
    login_challenge: str,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/login/accept".format(_client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[CompletedRequest, GenericError]]:
    if response.status_code == 200:
        response_200 = CompletedRequest.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GenericError.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = GenericError.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CompletedRequest, GenericError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    json_body: AcceptLoginRequest,
    login_challenge: str,
) -> Response[Union[CompletedRequest, GenericError]]:
    """Accept a Login Request

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

    This endpoint tells ORY Hydra that the subject has successfully authenticated and includes
    additional information such as
    the subject's ID and if ORY Hydra should remember the subject's subject agent for future
    authentication attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (AcceptLoginRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
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

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    json_body: AcceptLoginRequest,
    login_challenge: str,
) -> Optional[Union[CompletedRequest, GenericError]]:
    """Accept a Login Request

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

    This endpoint tells ORY Hydra that the subject has successfully authenticated and includes
    additional information such as
    the subject's ID and if ORY Hydra should remember the subject's subject agent for future
    authentication attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (AcceptLoginRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """

    return sync_detailed(
        _client=_client,
        json_body=json_body,
        login_challenge=login_challenge,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    json_body: AcceptLoginRequest,
    login_challenge: str,
) -> Response[Union[CompletedRequest, GenericError]]:
    """Accept a Login Request

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

    This endpoint tells ORY Hydra that the subject has successfully authenticated and includes
    additional information such as
    the subject's ID and if ORY Hydra should remember the subject's subject agent for future
    authentication attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (AcceptLoginRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
        login_challenge=login_challenge,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    json_body: AcceptLoginRequest,
    login_challenge: str,
) -> Optional[Union[CompletedRequest, GenericError]]:
    """Accept a Login Request

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

    This endpoint tells ORY Hydra that the subject has successfully authenticated and includes
    additional information such as
    the subject's ID and if ORY Hydra should remember the subject's subject agent for future
    authentication attempts by setting
    a cookie.

    The response contains a redirect URL which the login provider should redirect the user-agent to.

    Args:
        login_challenge (str):
        json_body (AcceptLoginRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            json_body=json_body,
            login_challenge=login_challenge,
        )
    ).parsed
