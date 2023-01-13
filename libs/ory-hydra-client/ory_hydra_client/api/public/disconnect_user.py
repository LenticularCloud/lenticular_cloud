from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET




def _get_kwargs(
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/oauth2/sessions/logout".format(
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




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    _client: Client,

) -> Response[Any]:
    """OpenID Connect Front-Backchannel Enabled Logout

     This endpoint initiates and completes user logout at ORY Hydra and initiates OpenID Connect
    Front-/Back-channel logout:

    https://openid.net/specs/openid-connect-frontchannel-1_0.html
    https://openid.net/specs/openid-connect-backchannel-1_0.html

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    _client: Client,

) -> Response[Any]:
    """OpenID Connect Front-Backchannel Enabled Logout

     This endpoint initiates and completes user logout at ORY Hydra and initiates OpenID Connect
    Front-/Back-channel logout:

    https://openid.net/specs/openid-connect-frontchannel-1_0.html
    https://openid.net/specs/openid-connect-backchannel-1_0.html

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)


