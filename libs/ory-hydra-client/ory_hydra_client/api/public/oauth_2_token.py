from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import Dict
from ...models.oauth_2_token_response import Oauth2TokenResponse
from typing import cast
from ...models.oauth_2_token_data import Oauth2TokenData
from ...models.generic_error import GenericError



def _get_kwargs(
    *,
    _client: AuthenticatedClient,

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
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, Oauth2TokenResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Oauth2TokenResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GenericError.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GenericError.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, Oauth2TokenResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[GenericError, Oauth2TokenResponse]]:
    """The OAuth 2.0 Token Endpoint

     The client makes a request to the token endpoint by sending the
    following parameters using the \"application/x-www-form-urlencoded\" HTTP
    request entity-body.

    > Do not implement a client for this endpoint yourself. Use a library. There are many libraries
    > available for any programming language. You can find a list of libraries here:
    https://oauth.net/code/
    >
    > Do note that Hydra SDK does not implement this endpoint properly. Use one of the libraries listed
    above!

    Returns:
        Response[Union[GenericError, Oauth2TokenResponse]]
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
    _client: AuthenticatedClient,

) -> Optional[Union[GenericError, Oauth2TokenResponse]]:
    """The OAuth 2.0 Token Endpoint

     The client makes a request to the token endpoint by sending the
    following parameters using the \"application/x-www-form-urlencoded\" HTTP
    request entity-body.

    > Do not implement a client for this endpoint yourself. Use a library. There are many libraries
    > available for any programming language. You can find a list of libraries here:
    https://oauth.net/code/
    >
    > Do note that Hydra SDK does not implement this endpoint properly. Use one of the libraries listed
    above!

    Returns:
        Response[Union[GenericError, Oauth2TokenResponse]]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[GenericError, Oauth2TokenResponse]]:
    """The OAuth 2.0 Token Endpoint

     The client makes a request to the token endpoint by sending the
    following parameters using the \"application/x-www-form-urlencoded\" HTTP
    request entity-body.

    > Do not implement a client for this endpoint yourself. Use a library. There are many libraries
    > available for any programming language. You can find a list of libraries here:
    https://oauth.net/code/
    >
    > Do note that Hydra SDK does not implement this endpoint properly. Use one of the libraries listed
    above!

    Returns:
        Response[Union[GenericError, Oauth2TokenResponse]]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: AuthenticatedClient,

) -> Optional[Union[GenericError, Oauth2TokenResponse]]:
    """The OAuth 2.0 Token Endpoint

     The client makes a request to the token endpoint by sending the
    following parameters using the \"application/x-www-form-urlencoded\" HTTP
    request entity-body.

    > Do not implement a client for this endpoint yourself. Use a library. There are many libraries
    > available for any programming language. You can find a list of libraries here:
    https://oauth.net/code/
    >
    > Do note that Hydra SDK does not implement this endpoint properly. Use one of the libraries listed
    above!

    Returns:
        Response[Union[GenericError, Oauth2TokenResponse]]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

