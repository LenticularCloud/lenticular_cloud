from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from typing import cast
from ...models.o_auth_2_client import OAuth2Client
from typing import Dict



def _get_kwargs(
    *,
    _client: Client,
    json_body: OAuth2Client,

) -> Dict[str, Any]:
    url = "{}/clients".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, OAuth2Client]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = OAuth2Client.from_dict(response.json())



        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GenericError.from_dict(response.json())



        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = GenericError.from_dict(response.json())



        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = GenericError.from_dict(response.json())



        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, OAuth2Client]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    _client: Client,
    json_body: OAuth2Client,

) -> Response[Union[GenericError, OAuth2Client]]:
    """Create an OAuth 2.0 Client

     Create a new OAuth 2.0 client If you pass `client_secret` the secret will be used, otherwise a
    random secret will be generated. The secret will be returned in the response and you will not be
    able to retrieve it later on. Write the secret down and keep it somwhere safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
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
    json_body: OAuth2Client,

) -> Optional[Union[GenericError, OAuth2Client]]:
    """Create an OAuth 2.0 Client

     Create a new OAuth 2.0 client If you pass `client_secret` the secret will be used, otherwise a
    random secret will be generated. The secret will be returned in the response and you will not be
    able to retrieve it later on. Write the secret down and keep it somwhere safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
    """


    return sync_detailed(
        _client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    *,
    _client: Client,
    json_body: OAuth2Client,

) -> Response[Union[GenericError, OAuth2Client]]:
    """Create an OAuth 2.0 Client

     Create a new OAuth 2.0 client If you pass `client_secret` the secret will be used, otherwise a
    random secret will be generated. The secret will be returned in the response and you will not be
    able to retrieve it later on. Write the secret down and keep it somwhere safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
    """


    kwargs = _get_kwargs(
        _client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    *,
    _client: Client,
    json_body: OAuth2Client,

) -> Optional[Union[GenericError, OAuth2Client]]:
    """Create an OAuth 2.0 Client

     Create a new OAuth 2.0 client If you pass `client_secret` the secret will be used, otherwise a
    random secret will be generated. The secret will be returned in the response and you will not be
    able to retrieve it later on. Write the secret down and keep it somwhere safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
    To manage ORY Hydra, you will need an OAuth 2.0 Client as well. Make sure that this endpoint is well
    protected and only callable by first-party components.

    Args:
        json_body (OAuth2Client):

    Returns:
        Response[Union[GenericError, OAuth2Client]]
    """


    return (await asyncio_detailed(
        _client=_client,
json_body=json_body,

    )).parsed

