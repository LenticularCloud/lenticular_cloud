from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.json_web_key_set import JsonWebKeySet



def _get_kwargs(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/admin/keys/{set}/{kid}".format(
        _client.base_url,set=set_,kid=kid)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[JsonWebKeySet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JsonWebKeySet.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[JsonWebKeySet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Response[JsonWebKeySet]:
    """Get JSON Web Key

     This endpoint returns a singular JSON Web Key contained in a set. It is identified by the set and
    the specific key ID (kid).

    Args:
        set_ (str):
        kid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
_client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Optional[JsonWebKeySet]:
    """Get JSON Web Key

     This endpoint returns a singular JSON Web Key contained in a set. It is identified by the set and
    the specific key ID (kid).

    Args:
        set_ (str):
        kid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return sync_detailed(
        set_=set_,
kid=kid,
_client=_client,

    ).parsed

async def asyncio_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Response[JsonWebKeySet]:
    """Get JSON Web Key

     This endpoint returns a singular JSON Web Key contained in a set. It is identified by the set and
    the specific key ID (kid).

    Args:
        set_ (str):
        kid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
_client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Optional[JsonWebKeySet]:
    """Get JSON Web Key

     This endpoint returns a singular JSON Web Key contained in a set. It is identified by the set and
    the specific key ID (kid).

    Args:
        set_ (str):
        kid (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return (await asyncio_detailed(
        set_=set_,
kid=kid,
_client=_client,

    )).parsed

