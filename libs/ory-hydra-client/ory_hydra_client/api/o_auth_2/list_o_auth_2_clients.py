from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from ...models import OAuth20Client
from typing import Optional
from typing import Union



def _get_kwargs(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    client_name: Union[Unset, None, str] = UNSET,
    owner: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/admin/clients".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["page_size"] = page_size


    params["page_token"] = page_token


    params["client_name"] = client_name


    params["owner"] = owner



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List[OAuth20Client]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = list([ OAuth20Client.from_dict(data) for data in response.json() ])
        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List[OAuth20Client]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    client_name: Union[Unset, None, str] = UNSET,
    owner: Union[Unset, None, str] = UNSET,

) -> Response[List[OAuth20Client]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets.
    As a default it lists the first 100 clients.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        client_name (Union[Unset, None, str]):
        owner (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,
page_size=page_size,
page_token=page_token,
client_name=client_name,
owner=owner,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)


async def asyncio_detailed(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    client_name: Union[Unset, None, str] = UNSET,
    owner: Union[Unset, None, str] = UNSET,

) -> Response[List[OAuth20Client]]:
    """List OAuth 2.0 Clients

     This endpoint lists all clients in the database, and never returns client secrets.
    As a default it lists the first 100 clients.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        client_name (Union[Unset, None, str]):
        owner (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,
page_size=page_size,
page_token=page_token,
client_name=client_name,
owner=owner,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)


