from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.well_known import WellKnown
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/.well-known/openid-configuration".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, WellKnown]]:
    if response.status_code == 200:
        response_200 = WellKnown.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, WellKnown]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, WellKnown]]:
    """OpenID Connect Discovery

     The well known endpoint an be used to retrieve information for OpenID Connect clients. We encourage
    you to not roll
    your own OpenID Connect client but to use an OpenID Connect client library instead. You can learn
    more on this
    flow at https://openid.net/specs/openid-connect-discovery-1_0.html .

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Returns:
        Response[Union[GenericError, WellKnown]]
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
) -> Optional[Union[GenericError, WellKnown]]:
    """OpenID Connect Discovery

     The well known endpoint an be used to retrieve information for OpenID Connect clients. We encourage
    you to not roll
    your own OpenID Connect client but to use an OpenID Connect client library instead. You can learn
    more on this
    flow at https://openid.net/specs/openid-connect-discovery-1_0.html .

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Returns:
        Response[Union[GenericError, WellKnown]]
    """

    return sync_detailed(
        _client=_client,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
) -> Response[Union[GenericError, WellKnown]]:
    """OpenID Connect Discovery

     The well known endpoint an be used to retrieve information for OpenID Connect clients. We encourage
    you to not roll
    your own OpenID Connect client but to use an OpenID Connect client library instead. You can learn
    more on this
    flow at https://openid.net/specs/openid-connect-discovery-1_0.html .

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Returns:
        Response[Union[GenericError, WellKnown]]
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
) -> Optional[Union[GenericError, WellKnown]]:
    """OpenID Connect Discovery

     The well known endpoint an be used to retrieve information for OpenID Connect clients. We encourage
    you to not roll
    your own OpenID Connect client but to use an OpenID Connect client library instead. You can learn
    more on this
    flow at https://openid.net/specs/openid-connect-discovery-1_0.html .

    Popular libraries for OpenID Connect clients include oidc-client-js (JavaScript), go-oidc (Golang),
    and others.
    For a full list of clients go here: https://openid.net/developers/certified/

    Returns:
        Response[Union[GenericError, WellKnown]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
        )
    ).parsed
