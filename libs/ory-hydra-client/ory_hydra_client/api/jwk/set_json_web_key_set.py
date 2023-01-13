from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import cast
from typing import Dict
from ...models.json_web_key_set import JsonWebKeySet



def _get_kwargs(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySet,

) -> Dict[str, Any]:
    url = "{}/admin/keys/{set}".format(
        _client.base_url,set=set_)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    

    

    

    json_json_body = json_body.to_dict()



    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[JsonWebKeySet]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JsonWebKeySet.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[JsonWebKeySet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySet,

) -> Response[JsonWebKeySet]:
    """Update a JSON Web Key Set

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySet): JSON Web Key Set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    kwargs = _get_kwargs(
        set_=set_,
_client=_client,
json_body=json_body,

    )

    response = httpx.request(
        verify=_client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=_client, response=response)

def sync(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySet,

) -> Optional[JsonWebKeySet]:
    """Update a JSON Web Key Set

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySet): JSON Web Key Set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return sync_detailed(
        set_=set_,
_client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySet,

) -> Response[JsonWebKeySet]:
    """Update a JSON Web Key Set

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySet): JSON Web Key Set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    kwargs = _get_kwargs(
        set_=set_,
_client=_client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(client=_client, response=response)

async def asyncio(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySet,

) -> Optional[JsonWebKeySet]:
    """Update a JSON Web Key Set

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySet): JSON Web Key Set

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKeySet]
    """


    return (await asyncio_detailed(
        set_=set_,
_client=_client,
json_body=json_body,

    )).parsed

