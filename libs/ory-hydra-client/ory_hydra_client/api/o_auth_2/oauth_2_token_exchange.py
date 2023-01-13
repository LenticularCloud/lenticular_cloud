from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.o_auth_2_token_exchange import OAuth2TokenExchange
from typing import Dict
from typing import cast
from ...models.oauth_2_token_exchange_data import Oauth2TokenExchangeData



def _get_kwargs(
    *,
    _client: AuthenticatedClient,
    form_data: Oauth2TokenExchangeData,

) -> Dict[str, Any]:
    url = "{}/oauth2/token".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[OAuth2TokenExchange]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuth2TokenExchange.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[OAuth2TokenExchange]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,
    form_data: Oauth2TokenExchangeData,

) -> Response[OAuth2TokenExchange]:
    """The OAuth 2.0 Token Endpoint

     Use open source libraries to perform OAuth 2.0 and OpenID Connect
    available for any programming language. You can find a list of libraries here
    https://oauth.net/code/

    The Ory SDK is not yet able to this endpoint properly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2TokenExchange]
    """


    kwargs = _get_kwargs(
        _client=_client,
form_data=form_data,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: AuthenticatedClient,
    form_data: Oauth2TokenExchangeData,

) -> Optional[OAuth2TokenExchange]:
    """The OAuth 2.0 Token Endpoint

     Use open source libraries to perform OAuth 2.0 and OpenID Connect
    available for any programming language. You can find a list of libraries here
    https://oauth.net/code/

    The Ory SDK is not yet able to this endpoint properly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2TokenExchange]
    """


    return sync_detailed(
        _client=_client,
form_data=form_data,

    ).parsed

async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,
    form_data: Oauth2TokenExchangeData,

) -> Response[OAuth2TokenExchange]:
    """The OAuth 2.0 Token Endpoint

     Use open source libraries to perform OAuth 2.0 and OpenID Connect
    available for any programming language. You can find a list of libraries here
    https://oauth.net/code/

    The Ory SDK is not yet able to this endpoint properly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2TokenExchange]
    """


    kwargs = _get_kwargs(
        _client=_client,
form_data=form_data,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: AuthenticatedClient,
    form_data: Oauth2TokenExchangeData,

) -> Optional[OAuth2TokenExchange]:
    """The OAuth 2.0 Token Endpoint

     Use open source libraries to perform OAuth 2.0 and OpenID Connect
    available for any programming language. You can find a list of libraries here
    https://oauth.net/code/

    The Ory SDK is not yet able to this endpoint properly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OAuth2TokenExchange]
    """


    return (await asyncio_detailed(
        _client=_client,
form_data=form_data,

    )).parsed

