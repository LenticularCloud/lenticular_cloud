from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.introspected_o_auth_2_token import IntrospectedOAuth2Token
from ...models.introspect_o_auth_2_token_data import IntrospectOAuth2TokenData
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,
    form_data: IntrospectOAuth2TokenData,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/introspect".format(
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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[IntrospectedOAuth2Token]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IntrospectedOAuth2Token.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[IntrospectedOAuth2Token]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    form_data: IntrospectOAuth2TokenData,

) -> Response[IntrospectedOAuth2Token]:
    """Introspect OAuth2 Access and Refresh Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `session.access_token` during the consent flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectedOAuth2Token]
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
    _client: Client,
    form_data: IntrospectOAuth2TokenData,

) -> Optional[IntrospectedOAuth2Token]:
    """Introspect OAuth2 Access and Refresh Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `session.access_token` during the consent flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectedOAuth2Token]
    """


    return sync_detailed(
        _client=_client,
form_data=form_data,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    form_data: IntrospectOAuth2TokenData,

) -> Response[IntrospectedOAuth2Token]:
    """Introspect OAuth2 Access and Refresh Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `session.access_token` during the consent flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectedOAuth2Token]
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
    _client: Client,
    form_data: IntrospectOAuth2TokenData,

) -> Optional[IntrospectedOAuth2Token]:
    """Introspect OAuth2 Access and Refresh Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `session.access_token` during the consent flow.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IntrospectedOAuth2Token]
    """


    return (await asyncio_detailed(
        _client=_client,
form_data=form_data,

    )).parsed

