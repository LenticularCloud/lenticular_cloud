from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.revoke_o_auth_2_token_data import RevokeOAuth2TokenData
from typing import Dict
from typing import cast



def _get_kwargs(
    *,
    _client: AuthenticatedClient,
    form_data: RevokeOAuth2TokenData,

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
        "data": form_data.to_dict(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
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
    _client: AuthenticatedClient,
    form_data: RevokeOAuth2TokenData,

) -> Response[Any]:
    """Revoke OAuth 2.0 Access or Refresh Token

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    _client: AuthenticatedClient,
    form_data: RevokeOAuth2TokenData,

) -> Response[Any]:
    """Revoke OAuth 2.0 Access or Refresh Token

     Revoking a token (both access and refresh) means that the tokens will be invalid. A revoked access
    token can no
    longer be used to make access requests, and a revoked refresh token can no longer be used to refresh
    an access token.
    Revoking a refresh token also invalidates the access token that was created with it. A token may
    only be revoked by
    the client the token was generated for.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


