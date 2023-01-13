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
from ...models.o_auth_20_consent_session import OAuth20ConsentSession
from typing import cast, List



def _get_kwargs(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    subject: str,
    login_session_id: Union[Unset, None, str] = UNSET,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/sessions/consent".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["page_size"] = page_size


    params["page_token"] = page_token


    params["subject"] = subject


    params["login_session_id"] = login_session_id



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List['OAuth20ConsentSession']]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemaso_auth_2_consent_sessions_item_data in (_response_200):
            componentsschemaso_auth_2_consent_sessions_item = OAuth20ConsentSession.from_dict(componentsschemaso_auth_2_consent_sessions_item_data)



            response_200.append(componentsschemaso_auth_2_consent_sessions_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List['OAuth20ConsentSession']]:
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
    subject: str,
    login_session_id: Union[Unset, None, str] = UNSET,

) -> Response[List['OAuth20ConsentSession']]:
    """List OAuth 2.0 Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        subject (str):
        login_session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth20ConsentSession']]
    """


    kwargs = _get_kwargs(
        _client=_client,
page_size=page_size,
page_token=page_token,
subject=subject,
login_session_id=login_session_id,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    subject: str,
    login_session_id: Union[Unset, None, str] = UNSET,

) -> Optional[List['OAuth20ConsentSession']]:
    """List OAuth 2.0 Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        subject (str):
        login_session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth20ConsentSession']]
    """


    return sync_detailed(
        _client=_client,
page_size=page_size,
page_token=page_token,
subject=subject,
login_session_id=login_session_id,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    subject: str,
    login_session_id: Union[Unset, None, str] = UNSET,

) -> Response[List['OAuth20ConsentSession']]:
    """List OAuth 2.0 Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        subject (str):
        login_session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth20ConsentSession']]
    """


    kwargs = _get_kwargs(
        _client=_client,
page_size=page_size,
page_token=page_token,
subject=subject,
login_session_id=login_session_id,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    page_size: Union[Unset, None, int] = 250,
    page_token: Union[Unset, None, str] = '1',
    subject: str,
    login_session_id: Union[Unset, None, str] = UNSET,

) -> Optional[List['OAuth20ConsentSession']]:
    """List OAuth 2.0 Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.

    Args:
        page_size (Union[Unset, None, int]):  Default: 250.
        page_token (Union[Unset, None, str]):  Default: '1'.
        subject (str):
        login_session_id (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['OAuth20ConsentSession']]
    """


    return (await asyncio_detailed(
        _client=_client,
page_size=page_size,
page_token=page_token,
subject=subject,
login_session_id=login_session_id,

    )).parsed

