from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.consent_request import ConsentRequest
from ...models.generic_error import GenericError
from ...types import UNSET, Response


def _get_kwargs(
    *,
    _client: Client,
    consent_challenge: str,
) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/consent".format(_client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    params: Dict[str, Any] = {}
    params["consent_challenge"] = consent_challenge

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ConsentRequest, GenericError]]:
    if response.status_code == 200:
        response_200 = ConsentRequest.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = GenericError.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = GenericError.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ConsentRequest, GenericError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    consent_challenge: str,
) -> Response[Union[ConsentRequest, GenericError]]:
    """Get Consent Request Information

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    to authenticate the subject and then tell ORY Hydra now about it. If the subject authenticated,
    he/she must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent provider which handles this request and is a web app implemented and hosted by you. It
    shows a subject interface which asks the subject to
    grant or deny the client access to the requested scope (\"Application my-dropbox-app wants write
    access to all your private files\").

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells ORY Hydra if
    the subject accepted
    or rejected the request.

    Args:
        consent_challenge (str):

    Returns:
        Response[Union[ConsentRequest, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        consent_challenge=consent_challenge,
    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    _client: Client,
    consent_challenge: str,
) -> Optional[Union[ConsentRequest, GenericError]]:
    """Get Consent Request Information

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    to authenticate the subject and then tell ORY Hydra now about it. If the subject authenticated,
    he/she must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent provider which handles this request and is a web app implemented and hosted by you. It
    shows a subject interface which asks the subject to
    grant or deny the client access to the requested scope (\"Application my-dropbox-app wants write
    access to all your private files\").

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells ORY Hydra if
    the subject accepted
    or rejected the request.

    Args:
        consent_challenge (str):

    Returns:
        Response[Union[ConsentRequest, GenericError]]
    """

    return sync_detailed(
        _client=_client,
        consent_challenge=consent_challenge,
    ).parsed


async def asyncio_detailed(
    *,
    _client: Client,
    consent_challenge: str,
) -> Response[Union[ConsentRequest, GenericError]]:
    """Get Consent Request Information

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    to authenticate the subject and then tell ORY Hydra now about it. If the subject authenticated,
    he/she must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent provider which handles this request and is a web app implemented and hosted by you. It
    shows a subject interface which asks the subject to
    grant or deny the client access to the requested scope (\"Application my-dropbox-app wants write
    access to all your private files\").

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells ORY Hydra if
    the subject accepted
    or rejected the request.

    Args:
        consent_challenge (str):

    Returns:
        Response[Union[ConsentRequest, GenericError]]
    """

    kwargs = _get_kwargs(
        _client=_client,
        consent_challenge=consent_challenge,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    _client: Client,
    consent_challenge: str,
) -> Optional[Union[ConsentRequest, GenericError]]:
    """Get Consent Request Information

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, ORY Hydra asks the
    login provider
    to authenticate the subject and then tell ORY Hydra now about it. If the subject authenticated,
    he/she must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent provider which handles this request and is a web app implemented and hosted by you. It
    shows a subject interface which asks the subject to
    grant or deny the client access to the requested scope (\"Application my-dropbox-app wants write
    access to all your private files\").

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells ORY Hydra if
    the subject accepted
    or rejected the request.

    Args:
        consent_challenge (str):

    Returns:
        Response[Union[ConsentRequest, GenericError]]
    """

    return (
        await asyncio_detailed(
            _client=_client,
            consent_challenge=consent_challenge,
        )
    ).parsed
