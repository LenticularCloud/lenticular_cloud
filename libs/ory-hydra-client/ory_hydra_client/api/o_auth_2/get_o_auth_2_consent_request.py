from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.o_auth_20_redirect_browser_to import OAuth20RedirectBrowserTo
from ...models.contains_information_on_an_ongoing_consent_request import ContainsInformationOnAnOngoingConsentRequest
from typing import cast
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,
    consent_challenge: str,

) -> Dict[str, Any]:
    url = "{}/admin/oauth2/auth/requests/consent".format(
        _client.base_url)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ContainsInformationOnAnOngoingConsentRequest.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.GONE:
        response_410 = OAuth20RedirectBrowserTo.from_dict(response.json())



        return response_410
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    consent_challenge: str,

) -> Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Consent Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell Ory now about it. If the subject authenticated, he/she
    must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells Ory if the
    subject accepted
    or rejected the request.

    The default consent provider is available via the Ory Managed Account Experience. To customize the
    consent provider, please
    head over to the OAuth 2.0 documentation.

    Args:
        consent_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]
    """


    kwargs = _get_kwargs(
        _client=_client,
consent_challenge=consent_challenge,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    *,
    _client: Client,
    consent_challenge: str,

) -> Optional[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Consent Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell Ory now about it. If the subject authenticated, he/she
    must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells Ory if the
    subject accepted
    or rejected the request.

    The default consent provider is available via the Ory Managed Account Experience. To customize the
    consent provider, please
    head over to the OAuth 2.0 documentation.

    Args:
        consent_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]
    """


    return sync_detailed(
        _client=_client,
consent_challenge=consent_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    consent_challenge: str,

) -> Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Consent Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell Ory now about it. If the subject authenticated, he/she
    must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells Ory if the
    subject accepted
    or rejected the request.

    The default consent provider is available via the Ory Managed Account Experience. To customize the
    consent provider, please
    head over to the OAuth 2.0 documentation.

    Args:
        consent_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]
    """


    kwargs = _get_kwargs(
        _client=_client,
consent_challenge=consent_challenge,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    *,
    _client: Client,
    consent_challenge: str,

) -> Optional[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]:
    """Get OAuth 2.0 Consent Request

     When an authorization code, hybrid, or implicit OAuth 2.0 Flow is initiated, Ory asks the login
    provider
    to authenticate the subject and then tell Ory now about it. If the subject authenticated, he/she
    must now be asked if
    the OAuth 2.0 Client which initiated the flow should be allowed to access the resources on the
    subject's behalf.

    The consent challenge is appended to the consent provider's URL to which the subject's user-agent
    (browser) is redirected to. The consent
    provider uses that challenge to fetch information on the OAuth2 request and then tells Ory if the
    subject accepted
    or rejected the request.

    The default consent provider is available via the Ory Managed Account Experience. To customize the
    consent provider, please
    head over to the OAuth 2.0 documentation.

    Args:
        consent_challenge (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ContainsInformationOnAnOngoingConsentRequest, OAuth20RedirectBrowserTo]]
    """


    return (await asyncio_detailed(
        _client=_client,
consent_challenge=consent_challenge,

    )).parsed

