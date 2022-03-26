from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.reject_request import RejectRequest
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    form_data: RejectRequest,
    json_body: RejectRequest,
    logout_challenge: str,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/logout/reject".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["logout_challenge"] = logout_challenge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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
    form_data: RejectRequest,
    json_body: RejectRequest,
    logout_challenge: str,
) -> Response[Union[Any, GenericError]]:
    """Reject a Logout Request

     When a user or an application requests ORY Hydra to log out a user, this endpoint is used to deny
    that logout request.
    No body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):
        json_body (RejectRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        form_data=form_data,
        json_body=json_body,
        logout_challenge=logout_challenge,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    form_data: RejectRequest,
    json_body: RejectRequest,
    logout_challenge: str,
) -> Optional[Union[Any, GenericError]]:
    """Reject a Logout Request

     When a user or an application requests ORY Hydra to log out a user, this endpoint is used to deny
    that logout request.
    No body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):
        json_body (RejectRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return sync_detailed(
        _client=_client,
        form_data=form_data,
        json_body=json_body,
        logout_challenge=logout_challenge,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    form_data: RejectRequest,
    json_body: RejectRequest,
    logout_challenge: str,
) -> Response[Union[Any, GenericError]]:
    """Reject a Logout Request

     When a user or an application requests ORY Hydra to log out a user, this endpoint is used to deny
    that logout request.
    No body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):
        json_body (RejectRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        form_data=form_data,
        json_body=json_body,
        logout_challenge=logout_challenge,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    form_data: RejectRequest,
    json_body: RejectRequest,
    logout_challenge: str,
) -> Optional[Union[Any, GenericError]]:
    """Reject a Logout Request

     When a user or an application requests ORY Hydra to log out a user, this endpoint is used to deny
    that logout request.
    No body is required.

    The response is empty as the logout provider has to chose what action to perform next.

    Args:
        logout_challenge (str):
        json_body (RejectRequest):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            form_data=form_data,
            json_body=json_body,
            logout_challenge=logout_challenge,
        )
    ).parsed