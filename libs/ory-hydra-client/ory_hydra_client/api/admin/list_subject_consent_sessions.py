from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.previous_consent_session import PreviousConsentSession
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    subject: str,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/sessions/consent".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, List[PreviousConsentSession]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PreviousConsentSession.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = GenericError.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, List[PreviousConsentSession]]]:
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
) -> Response[Union[GenericError, List[PreviousConsentSession]]]:
    """Lists All Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.


    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-
    url/admin/oauth2/auth/sessions/consent?subject={user}&limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        subject (str):

    Returns:
        Response[Union[GenericError, List[PreviousConsentSession]]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        subject=subject,
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
) -> Optional[Union[GenericError, List[PreviousConsentSession]]]:
    """Lists All Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.


    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-
    url/admin/oauth2/auth/sessions/consent?subject={user}&limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        subject (str):

    Returns:
        Response[Union[GenericError, List[PreviousConsentSession]]]
    """

    return sync_detailed(
        _client=_client,
        subject=subject,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    subject: str,
) -> Response[Union[GenericError, List[PreviousConsentSession]]]:
    """Lists All Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.


    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-
    url/admin/oauth2/auth/sessions/consent?subject={user}&limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        subject (str):

    Returns:
        Response[Union[GenericError, List[PreviousConsentSession]]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        subject=subject,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    subject: str,
) -> Optional[Union[GenericError, List[PreviousConsentSession]]]:
    """Lists All Consent Sessions of a Subject

     This endpoint lists all subject's granted consent sessions, including client and granted scope.
    If the subject is unknown or has not granted any consent sessions yet, the endpoint returns an
    empty JSON array with status code 200 OK.


    The \"Link\" header is also included in successful responses, which contains one or more links for
    pagination, formatted like so: '<https://hydra-
    url/admin/oauth2/auth/sessions/consent?subject={user}&limit={limit}&offset={offset}>;
    rel=\"{page}\"', where page is one of the following applicable pages: 'first', 'next', 'last', and
    'previous'.
    Multiple links can be included in this header, and will be separated by a comma.

    Args:
        subject (str):

    Returns:
        Response[Union[GenericError, List[PreviousConsentSession]]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            subject=subject,
        )
    ).parsed
