from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...types import UNSET, Unset
from typing import Optional
from typing import Union



def _get_kwargs(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/sessions/consent".format(
        _client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,

) -> Response[Any]:
    """Revoke OAuth 2.0 Consent Sessions of a Subject

     This endpoint revokes a subject's granted consent sessions and invalidates all
    associated OAuth 2.0 Access Tokens. You may also only revoke sessions for a specific OAuth 2.0
    Client ID.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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

    return _build_response(client=_client, response=response)


async def asyncio_detailed(
    *,
    _client: Client,
    subject: str,
    client: Union[Unset, None, str] = UNSET,
    all_: Union[Unset, None, bool] = UNSET,

) -> Response[Any]:
    """Revoke OAuth 2.0 Consent Sessions of a Subject

     This endpoint revokes a subject's granted consent sessions and invalidates all
    associated OAuth 2.0 Access Tokens. You may also only revoke sessions for a specific OAuth 2.0
    Client ID.

    Args:
        subject (str):
        client (Union[Unset, None, str]):
        all_ (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        _client=_client,
subject=subject,
client=client,
all_=all_,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)


