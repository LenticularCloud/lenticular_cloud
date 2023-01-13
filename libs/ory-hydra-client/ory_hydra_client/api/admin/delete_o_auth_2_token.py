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
    client_id: str,

) -> Dict[str, Any]:
    url = "{}/oauth2/tokens".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["client_id"] = client_id



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
    _client: Client,
    client_id: str,

) -> Response[Union[Any, GenericError]]:
    """Delete OAuth2 Access Tokens from a Client

     This endpoint deletes OAuth2 access tokens issued for a client from the database

    Args:
        client_id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
client_id=client_id,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    *,
    _client: Client,
    client_id: str,

) -> Optional[Union[Any, GenericError]]:
    """Delete OAuth2 Access Tokens from a Client

     This endpoint deletes OAuth2 access tokens issued for a client from the database

    Args:
        client_id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return sync_detailed(
        _client=_client,
client_id=client_id,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    client_id: str,

) -> Response[Union[Any, GenericError]]:
    """Delete OAuth2 Access Tokens from a Client

     This endpoint deletes OAuth2 access tokens issued for a client from the database

    Args:
        client_id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
client_id=client_id,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,
    client_id: str,

) -> Optional[Union[Any, GenericError]]:
    """Delete OAuth2 Access Tokens from a Client

     This endpoint deletes OAuth2 access tokens issued for a client from the database

    Args:
        client_id (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return (await asyncio_detailed(
        _client=_client,
client_id=client_id,

    )).parsed

