from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from ...models.revoke_o_auth_2_token_data import RevokeOAuth2TokenData
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: AuthenticatedClient,

) -> Dict[str, Any]:
    url = "{}/oauth2/revoke".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = cast(Any, None)
        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GenericError.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GenericError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[Any, GenericError]]:
    """Revoke OAuth2 Tokens

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Returns:
        Response[Union[Any, GenericError]]
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

) -> Optional[Union[Any, GenericError]]:
    """Revoke OAuth2 Tokens

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Returns:
        Response[Union[Any, GenericError]]
    """


    return sync_detailed(
        _client=_client,

    ).parsed

async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,

) -> Response[Union[Any, GenericError]]:
    """Revoke OAuth2 Tokens

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Returns:
        Response[Union[Any, GenericError]]
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

) -> Optional[Union[Any, GenericError]]:
    """Revoke OAuth2 Tokens

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Returns:
        Response[Union[Any, GenericError]]
    """


    return (await asyncio_detailed(
        _client=_client,

    )).parsed

