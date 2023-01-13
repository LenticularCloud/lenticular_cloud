from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.trusted_o_auth_2_jwt_grant_issuer import TrustedOAuth2JwtGrantIssuer
from typing import Dict
from typing import cast
from ...models.trust_o_auth_2_jwt_grant_issuer import TrustOAuth2JwtGrantIssuer



def _get_kwargs(
    *,
    _client: Client,
    json_body: TrustOAuth2JwtGrantIssuer,

) -> Dict[str, Any]:
    url = "{}/admin/trust/grants/jwt-bearer/issuers".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = TrustedOAuth2JwtGrantIssuer.from_dict(response.json())



        return response_201
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
    *,
    _client: Client,
    json_body: TrustOAuth2JwtGrantIssuer,

) -> Response[TrustedOAuth2JwtGrantIssuer]:
    """Trust OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to establish a trust relationship for a JWT issuer
    to perform JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication
    and Authorization Grants [RFC7523](https://datatracker.ietf.org/doc/html/rfc7523).

    Args:
        json_body (TrustOAuth2JwtGrantIssuer): Trust OAuth2 JWT Bearer Grant Type Issuer Request
            Body

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    json_body: TrustOAuth2JwtGrantIssuer,

) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    """Trust OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to establish a trust relationship for a JWT issuer
    to perform JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication
    and Authorization Grants [RFC7523](https://datatracker.ietf.org/doc/html/rfc7523).

    Args:
        json_body (TrustOAuth2JwtGrantIssuer): Trust OAuth2 JWT Bearer Grant Type Issuer Request
            Body

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    return sync_detailed(
        _client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    json_body: TrustOAuth2JwtGrantIssuer,

) -> Response[TrustedOAuth2JwtGrantIssuer]:
    """Trust OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to establish a trust relationship for a JWT issuer
    to perform JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication
    and Authorization Grants [RFC7523](https://datatracker.ietf.org/doc/html/rfc7523).

    Args:
        json_body (TrustOAuth2JwtGrantIssuer): Trust OAuth2 JWT Bearer Grant Type Issuer Request
            Body

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    json_body: TrustOAuth2JwtGrantIssuer,

) -> Optional[TrustedOAuth2JwtGrantIssuer]:
    """Trust OAuth2 JWT Bearer Grant Type Issuer

     Use this endpoint to establish a trust relationship for a JWT issuer
    to perform JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication
    and Authorization Grants [RFC7523](https://datatracker.ietf.org/doc/html/rfc7523).

    Args:
        json_body (TrustOAuth2JwtGrantIssuer): Trust OAuth2 JWT Bearer Grant Type Issuer Request
            Body

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TrustedOAuth2JwtGrantIssuer]
    """


    return (await asyncio_detailed(
        _client=_client,
json_body=json_body,

    )).parsed

