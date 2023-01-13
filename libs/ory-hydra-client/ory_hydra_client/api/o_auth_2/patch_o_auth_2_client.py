from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from ...models.o_auth_20_client import OAuth20Client
from typing import Dict
from ...models.json_patch import JsonPatch
from typing import cast, List



def _get_kwargs(
    id: str,
    *,
    _client: Client,
    json_body: List['JsonPatch'],

) -> Dict[str, Any]:
    url = "{}/admin/clients/{id}".format(
        _client.base_url,id=id)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    json_json_body = []
    for componentsschemasjson_patch_document_item_data in json_body:
        componentsschemasjson_patch_document_item = componentsschemasjson_patch_document_item_data.to_dict()

        json_json_body.append(componentsschemasjson_patch_document_item)






    

    return {
	    "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, OAuth20Client]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = OAuth20Client.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, OAuth20Client]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    _client: Client,
    json_body: List['JsonPatch'],

) -> Response[Union[Any, OAuth20Client]]:
    """Patch OAuth 2.0 Client

     Patch an existing OAuth 2.0 Client using JSON Patch. If you pass `client_secret`
    the secret will be updated and returned via the API. This is the
    only time you will be able to retrieve the client secret, so write it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):
        json_body (List['JsonPatch']): A JSONPatchDocument request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,
json_body=json_body,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    id: str,
    *,
    _client: Client,
    json_body: List['JsonPatch'],

) -> Optional[Union[Any, OAuth20Client]]:
    """Patch OAuth 2.0 Client

     Patch an existing OAuth 2.0 Client using JSON Patch. If you pass `client_secret`
    the secret will be updated and returned via the API. This is the
    only time you will be able to retrieve the client secret, so write it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):
        json_body (List['JsonPatch']): A JSONPatchDocument request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    return sync_detailed(
        id=id,
_client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    _client: Client,
    json_body: List['JsonPatch'],

) -> Response[Union[Any, OAuth20Client]]:
    """Patch OAuth 2.0 Client

     Patch an existing OAuth 2.0 Client using JSON Patch. If you pass `client_secret`
    the secret will be updated and returned via the API. This is the
    only time you will be able to retrieve the client secret, so write it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):
        json_body (List['JsonPatch']): A JSONPatchDocument request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    kwargs = _get_kwargs(
        id=id,
_client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    id: str,
    *,
    _client: Client,
    json_body: List['JsonPatch'],

) -> Optional[Union[Any, OAuth20Client]]:
    """Patch OAuth 2.0 Client

     Patch an existing OAuth 2.0 Client using JSON Patch. If you pass `client_secret`
    the secret will be updated and returned via the API. This is the
    only time you will be able to retrieve the client secret, so write it down and keep it safe.

    OAuth 2.0 clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients
    are
    generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.

    Args:
        id (str):
        json_body (List['JsonPatch']): A JSONPatchDocument request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OAuth20Client]]
    """


    return (await asyncio_detailed(
        id=id,
_client=_client,
json_body=json_body,

    )).parsed

