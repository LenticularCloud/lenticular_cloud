from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from typing import cast
from typing import Dict



def _get_kwargs(
    id: str,
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/clients/{id}".format(
        _client.base_url,id=id)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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
    id: str,
    *,
    _client: Client,

) -> Response[Union[Any, GenericError]]:
    """Deletes an OAuth 2.0 Client

     Delete an existing OAuth 2.0 Client by its ID.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    id: str,
    *,
    _client: Client,

) -> Optional[Union[Any, GenericError]]:
    """Deletes an OAuth 2.0 Client

     Delete an existing OAuth 2.0 Client by its ID.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return sync_detailed(
        id=id,
_client=_client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    _client: Client,

) -> Response[Union[Any, GenericError]]:
    """Deletes an OAuth 2.0 Client

     Delete an existing OAuth 2.0 Client by its ID.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    id: str,
    *,
    _client: Client,

) -> Optional[Union[Any, GenericError]]:
    """Deletes an OAuth 2.0 Client

     Delete an existing OAuth 2.0 Client by its ID.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return (await asyncio_detailed(
        id=id,
_client=_client,

    )).parsed

