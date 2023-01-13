from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from typing import cast
from ...models.trusted_o_auth_2_jwt_grant_issuer import TrustedOAuth2JwtGrantIssuer



def _get_kwargs(
    id: str,
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/admin/trust/grants/jwt-bearer/issuers/{id}".format(
        _client.base_url,id=id)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TrustedOAuth2JwtGrantIssuer.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[TrustedOAuth2JwtGrantIssuer]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    _client: Client,

) -> Response[TrustedOAuth2JwtGrantIssuer]:
    """Get Trusted OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to get a trusted JWT Bearer Grant Type Issuer. The ID is the one returned when you
    created the trust relationship.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    id: str,
    *,
    _client: Client,

) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    """Get Trusted OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to get a trusted JWT Bearer Grant Type Issuer. The ID is the one returned when you
    created the trust relationship.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    return sync_detailed(
        id=id,
_client=_client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    _client: Client,

) -> Response[TrustedOAuth2JwtGrantIssuer]:
    """Get Trusted OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to get a trusted JWT Bearer Grant Type Issuer. The ID is the one returned when you
    created the trust relationship.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    id: str,
    *,
    _client: Client,

) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    """Get Trusted OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to get a trusted JWT Bearer Grant Type Issuer. The ID is the one returned when you
    created the trust relationship.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    return (await asyncio_detailed(
        id=id,
_client=_client,

    )).parsed

