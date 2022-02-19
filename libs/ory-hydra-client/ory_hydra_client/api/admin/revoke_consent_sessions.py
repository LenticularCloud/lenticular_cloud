from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/sessions/consent".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["subject"] = subject

    params["client"] = client

    params["all"] = all_

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
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = GenericError.from_dict(response.json())

        return response_400
    if response.status_code == 404:
        response_404 = GenericError.from_dict(response.json())

        return response_404
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
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GenericError]]:
    """Revokes Consent Sessions of a Subject for a Specific OAuth 2.0 Client

     This endpoint revokes a subject's granted consent sessions for a specific OAuth 2.0 Client and
    invalidates all
    associated OAuth 2.0 Access Tokens.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        subject=subject,
        client=client,
        all_=all_,
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
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GenericError]]:
    """Revokes Consent Sessions of a Subject for a Specific OAuth 2.0 Client

     This endpoint revokes a subject's granted consent sessions for a specific OAuth 2.0 Client and
    invalidates all
    associated OAuth 2.0 Access Tokens.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return sync_detailed(
        _client=_client,
        subject=subject,
        client=client,
        all_=all_,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, GenericError]]:
    """Revokes Consent Sessions of a Subject for a Specific OAuth 2.0 Client

     This endpoint revokes a subject's granted consent sessions for a specific OAuth 2.0 Client and
    invalidates all
    associated OAuth 2.0 Access Tokens.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        subject=subject,
        client=client,
        all_=all_,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, GenericError]]:
    """Revokes Consent Sessions of a Subject for a Specific OAuth 2.0 Client

     This endpoint revokes a subject's granted consent sessions for a specific OAuth 2.0 Client and
    invalidates all
    associated OAuth 2.0 Access Tokens.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            subject=subject,
            client=client,
            all_=all_,
        )
    ).parsed
