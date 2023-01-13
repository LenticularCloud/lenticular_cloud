from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,
    subject: str,

) -> Dict[str, Any]:
    url = "{}/oauth2/auth/sessions/login".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["subject"] = subject



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GenericError.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GenericError.from_dict(response.json())



        return response_404
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
    _client: Client,
    subject: str,

) -> Response[Union[Any, GenericError]]:
    """Invalidates All Login Sessions of a Certain User
    Invalidates a Subject's Authentication Session

     This endpoint invalidates a subject's authentication session. After revoking the authentication
    session, the subject
    has to re-authenticate at ORY Hydra. This endpoint does not invalidate any tokens and does not work
    with OpenID Connect
    Front- or Back-channel logout.

    Args:
        subject (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
subject=subject,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    _client: Client,
    subject: str,

) -> Optional[Union[Any, GenericError]]:
    """Invalidates All Login Sessions of a Certain User
    Invalidates a Subject's Authentication Session

     This endpoint invalidates a subject's authentication session. After revoking the authentication
    session, the subject
    has to re-authenticate at ORY Hydra. This endpoint does not invalidate any tokens and does not work
    with OpenID Connect
    Front- or Back-channel logout.

    Args:
        subject (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return sync_detailed(
        _client=_client,
subject=subject,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    subject: str,

) -> Response[Union[Any, GenericError]]:
    """Invalidates All Login Sessions of a Certain User
    Invalidates a Subject's Authentication Session

     This endpoint invalidates a subject's authentication session. After revoking the authentication
    session, the subject
    has to re-authenticate at ORY Hydra. This endpoint does not invalidate any tokens and does not work
    with OpenID Connect
    Front- or Back-channel logout.

    Args:
        subject (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
subject=subject,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,
    subject: str,

) -> Optional[Union[Any, GenericError]]:
    """Invalidates All Login Sessions of a Certain User
    Invalidates a Subject's Authentication Session

     This endpoint invalidates a subject's authentication session. After revoking the authentication
    session, the subject
    has to re-authenticate at ORY Hydra. This endpoint does not invalidate any tokens and does not work
    with OpenID Connect
    Front- or Back-channel logout.

    Args:
        subject (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return (await asyncio_detailed(
        _client=_client,
subject=subject,

    )).parsed

