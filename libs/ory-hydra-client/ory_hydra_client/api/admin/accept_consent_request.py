from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from typing import Dict
from typing import cast
from ...models.completed_request import CompletedRequest
from ...models.generic_error import GenericError
from ...models.accept_consent_request import AcceptConsentRequest



def _get_kwargs(
    *,
    _client: Client,
    json_body: AcceptConsentRequest,
    consent_challenge: str,

) -> Dict[str, Any]:
    url = "{}/oauth2/auth/requests/consent/accept".format(
        _client.base_url)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["consent_challenge"] = consent_challenge



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    json_json_body = json_body.to_dict()



    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[CompletedRequest, GenericError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CompletedRequest.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = GenericError.from_dict(response.json())



        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[CompletedRequest, GenericError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    json_body: AcceptConsentRequest,
    consent_challenge: str,

) -> Response[Union[CompletedRequest, GenericError]]:
    """Accept a Consent Request

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

    This endpoint tells ORY Hydra that the subject has authorized the OAuth 2.0 client to access
    resources on his/her behalf.
    The consent provider includes additional information, such as session data for access and ID tokens,
    and if the
    consent request should be used as basis for future requests.

    The response contains a redirect URL which the consent provider should redirect the user-agent to.

    Args:
        consent_challenge (str):
        json_body (AcceptConsentRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,
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
    json_body: AcceptConsentRequest,
    consent_challenge: str,

) -> Optional[Union[CompletedRequest, GenericError]]:
    """Accept a Consent Request

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

    This endpoint tells ORY Hydra that the subject has authorized the OAuth 2.0 client to access
    resources on his/her behalf.
    The consent provider includes additional information, such as session data for access and ID tokens,
    and if the
    consent request should be used as basis for future requests.

    The response contains a redirect URL which the consent provider should redirect the user-agent to.

    Args:
        consent_challenge (str):
        json_body (AcceptConsentRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """


    return sync_detailed(
        _client=_client,
json_body=json_body,
consent_challenge=consent_challenge,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    json_body: AcceptConsentRequest,
    consent_challenge: str,

) -> Response[Union[CompletedRequest, GenericError]]:
    """Accept a Consent Request

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

    This endpoint tells ORY Hydra that the subject has authorized the OAuth 2.0 client to access
    resources on his/her behalf.
    The consent provider includes additional information, such as session data for access and ID tokens,
    and if the
    consent request should be used as basis for future requests.

    The response contains a redirect URL which the consent provider should redirect the user-agent to.

    Args:
        consent_challenge (str):
        json_body (AcceptConsentRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,
consent_challenge=consent_challenge,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,
    json_body: AcceptConsentRequest,
    consent_challenge: str,

) -> Optional[Union[CompletedRequest, GenericError]]:
    """Accept a Consent Request

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

    This endpoint tells ORY Hydra that the subject has authorized the OAuth 2.0 client to access
    resources on his/her behalf.
    The consent provider includes additional information, such as session data for access and ID tokens,
    and if the
    consent request should be used as basis for future requests.

    The response contains a redirect URL which the consent provider should redirect the user-agent to.

    Args:
        consent_challenge (str):
        json_body (AcceptConsentRequest):

    Returns:
        Response[Union[CompletedRequest, GenericError]]
    """


    return (await asyncio_detailed(
        _client=_client,
json_body=json_body,
consent_challenge=consent_challenge,

    )).parsed

