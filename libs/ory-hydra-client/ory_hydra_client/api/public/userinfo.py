from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.userinfo_response import UserinfoResponse
from ...models.generic_error import GenericError
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/userinfo".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, UserinfoResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserinfoResponse.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GenericError.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, UserinfoResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[GenericError, UserinfoResponse]]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including the idTokenExtra values, of
    the provided OAuth 2.0 Access Token.

    For more information please [refer to the spec](http://openid.net/specs/openid-connect-
    core-1_0.html#UserInfo).

    Returns:
        Response[Union[GenericError, UserinfoResponse]]
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

) -> Optional[Union[GenericError, UserinfoResponse]]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including the idTokenExtra values, of
    the provided OAuth 2.0 Access Token.

    For more information please [refer to the spec](http://openid.net/specs/openid-connect-
    core-1_0.html#UserInfo).

    Returns:
        Response[Union[GenericError, UserinfoResponse]]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[GenericError, UserinfoResponse]]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including the idTokenExtra values, of
    the provided OAuth 2.0 Access Token.

    For more information please [refer to the spec](http://openid.net/specs/openid-connect-
    core-1_0.html#UserInfo).

    Returns:
        Response[Union[GenericError, UserinfoResponse]]
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

) -> Optional[Union[GenericError, UserinfoResponse]]:
    """OpenID Connect Userinfo

     This endpoint returns the payload of the ID Token, including the idTokenExtra values, of
    the provided OAuth 2.0 Access Token.

    For more information please [refer to the spec](http://openid.net/specs/openid-connect-
    core-1_0.html#UserInfo).

    Returns:
        Response[Union[GenericError, UserinfoResponse]]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

