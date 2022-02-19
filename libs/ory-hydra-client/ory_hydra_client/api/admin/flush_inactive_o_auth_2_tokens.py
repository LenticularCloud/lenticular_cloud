from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.flush_inactive_o_auth_2_tokens_request import FlushInactiveOAuth2TokensRequest
from ...models.generic_error import GenericError
from ...types import Response


def _get_kwargs(
    *,
    _client: Client,
    json_body: FlushInactiveOAuth2TokensRequest,
) -> Dict[str, Any]:
    url = "{}/oauth2/flush".format(_client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 500:
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
    json_body: FlushInactiveOAuth2TokensRequest,
) -> Response[Union[Any, GenericError]]:
    """Flush Expired OAuth2 Access Tokens

     This endpoint flushes expired OAuth2 access tokens from the database. You can set a time after which
    no tokens will be
    not be touched, in case you want to keep recent tokens for auditing. Refresh tokens can not be
    flushed as they are deleted
    automatically when performing the refresh flow.

    Args:
        json_body (FlushInactiveOAuth2TokensRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    json_body: FlushInactiveOAuth2TokensRequest,
) -> Optional[Union[Any, GenericError]]:
    """Flush Expired OAuth2 Access Tokens

     This endpoint flushes expired OAuth2 access tokens from the database. You can set a time after which
    no tokens will be
    not be touched, in case you want to keep recent tokens for auditing. Refresh tokens can not be
    flushed as they are deleted
    automatically when performing the refresh flow.

    Args:
        json_body (FlushInactiveOAuth2TokensRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return sync_detailed(
        _client=_client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    json_body: FlushInactiveOAuth2TokensRequest,
) -> Response[Union[Any, GenericError]]:
    """Flush Expired OAuth2 Access Tokens

     This endpoint flushes expired OAuth2 access tokens from the database. You can set a time after which
    no tokens will be
    not be touched, in case you want to keep recent tokens for auditing. Refresh tokens can not be
    flushed as they are deleted
    automatically when performing the refresh flow.

    Args:
        json_body (FlushInactiveOAuth2TokensRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    json_body: FlushInactiveOAuth2TokensRequest,
) -> Optional[Union[Any, GenericError]]:
    """Flush Expired OAuth2 Access Tokens

     This endpoint flushes expired OAuth2 access tokens from the database. You can set a time after which
    no tokens will be
    not be touched, in case you want to keep recent tokens for auditing. Refresh tokens can not be
    flushed as they are deleted
    automatically when performing the refresh flow.

    Args:
        json_body (FlushInactiveOAuth2TokensRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            json_body=json_body,
        )
    ).parsed
