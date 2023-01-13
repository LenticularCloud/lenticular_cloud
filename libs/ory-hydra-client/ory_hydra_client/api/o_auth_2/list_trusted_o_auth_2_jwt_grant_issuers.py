from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Optional
from typing import Union
from typing import cast
from typing import Dict
from typing import cast, List
from ...models.trusted_o_auth_2_jwt_grant_issuer import TrustedOAuth2JwtGrantIssuer



def _get_kwargs(
    *,
    _client: Client,
    max_items: Union[Unset, None, int] = UNSET,
    default_items: Union[Unset, None, int] = UNSET,
    issuer: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/admin/trust/grants/jwt-bearer/issuers".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["MaxItems"] = max_items


    params["DefaultItems"] = default_items


    params["issuer"] = issuer



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List['TrustedOAuth2JwtGrantIssuer']]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemastrusted_o_auth_2_jwt_grant_issuers_item_data in (_response_200):
            componentsschemastrusted_o_auth_2_jwt_grant_issuers_item = TrustedOAuth2JwtGrantIssuer.from_dict(componentsschemastrusted_o_auth_2_jwt_grant_issuers_item_data)



            response_200.append(componentsschemastrusted_o_auth_2_jwt_grant_issuers_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List['TrustedOAuth2JwtGrantIssuer']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    max_items: Union[Unset, None, int] = UNSET,
    default_items: Union[Unset, None, int] = UNSET,
    issuer: Union[Unset, None, str] = UNSET,

) -> Response[List['TrustedOAuth2JwtGrantIssuer']]:
    """List Trusted OAuth2 JWT Bearer Grant Type Issuers

     Use this endpoint to list all trusted JWT Bearer Grant Type Issuers.

    Args:
        max_items (Union[Unset, None, int]):
        default_items (Union[Unset, None, int]):
        issuer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TrustedOAuth2JwtGrantIssuer']]
    """


    kwargs = _get_kwargs(
        _client=_client,
max_items=max_items,
default_items=default_items,
issuer=issuer,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    max_items: Union[Unset, None, int] = UNSET,
    default_items: Union[Unset, None, int] = UNSET,
    issuer: Union[Unset, None, str] = UNSET,

) -> Optional[List['TrustedOAuth2JwtGrantIssuer']]:
    """List Trusted OAuth2 JWT Bearer Grant Type Issuers

     Use this endpoint to list all trusted JWT Bearer Grant Type Issuers.

    Args:
        max_items (Union[Unset, None, int]):
        default_items (Union[Unset, None, int]):
        issuer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TrustedOAuth2JwtGrantIssuer']]
    """


    return sync_detailed(
        _client=_client,
max_items=max_items,
default_items=default_items,
issuer=issuer,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    max_items: Union[Unset, None, int] = UNSET,
    default_items: Union[Unset, None, int] = UNSET,
    issuer: Union[Unset, None, str] = UNSET,

) -> Response[List['TrustedOAuth2JwtGrantIssuer']]:
    """List Trusted OAuth2 JWT Bearer Grant Type Issuers

     Use this endpoint to list all trusted JWT Bearer Grant Type Issuers.

    Args:
        max_items (Union[Unset, None, int]):
        default_items (Union[Unset, None, int]):
        issuer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TrustedOAuth2JwtGrantIssuer']]
    """


    kwargs = _get_kwargs(
        _client=_client,
max_items=max_items,
default_items=default_items,
issuer=issuer,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    max_items: Union[Unset, None, int] = UNSET,
    default_items: Union[Unset, None, int] = UNSET,
    issuer: Union[Unset, None, str] = UNSET,

) -> Optional[List['TrustedOAuth2JwtGrantIssuer']]:
    """List Trusted OAuth2 JWT Bearer Grant Type Issuers

     Use this endpoint to list all trusted JWT Bearer Grant Type Issuers.

    Args:
        max_items (Union[Unset, None, int]):
        default_items (Union[Unset, None, int]):
        issuer (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['TrustedOAuth2JwtGrantIssuer']]
    """


    return (await asyncio_detailed(
        _client=_client,
max_items=max_items,
default_items=default_items,
issuer=issuer,

    )).parsed

