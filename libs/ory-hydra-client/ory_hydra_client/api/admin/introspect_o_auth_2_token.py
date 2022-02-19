from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.o_auth_2_token_introspection import OAuth2TokenIntrospection
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/oauth2/introspect".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, OAuth2TokenIntrospection]]:
    if response.status_code == 200:
        response_200 = OAuth2TokenIntrospection.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, OAuth2TokenIntrospection]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, OAuth2TokenIntrospection]]:
    """Introspect OAuth2 Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `accessTokenExtra` during the consent flow.

    For more information [read this blog post](https://www.oauth.com/oauth2-servers/token-introspection-
    endpoint/).

    Returns:
        Response[Union[GenericError, OAuth2TokenIntrospection]]
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
    _client: Client,
) -> Optional[Union[GenericError, OAuth2TokenIntrospection]]:
    """Introspect OAuth2 Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `accessTokenExtra` during the consent flow.

    For more information [read this blog post](https://www.oauth.com/oauth2-servers/token-introspection-
    endpoint/).

    Returns:
        Response[Union[GenericError, OAuth2TokenIntrospection]]
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, OAuth2TokenIntrospection]]:
    """Introspect OAuth2 Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `accessTokenExtra` during the consent flow.

    For more information [read this blog post](https://www.oauth.com/oauth2-servers/token-introspection-
    endpoint/).

    Returns:
        Response[Union[GenericError, OAuth2TokenIntrospection]]
    """

    kwargs = _get_kwargs(
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
) -> Optional[Union[GenericError, OAuth2TokenIntrospection]]:
    """Introspect OAuth2 Tokens

     The introspection endpoint allows to check if a token (both refresh and access) is active or not. An
    active token
    is neither expired nor revoked. If a token is active, additional information on the token will be
    included. You can
    set additional data for a token by setting `accessTokenExtra` during the consent flow.

    For more information [read this blog post](https://www.oauth.com/oauth2-servers/token-introspection-
    endpoint/).

    Returns:
        Response[Union[GenericError, OAuth2TokenIntrospection]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed
