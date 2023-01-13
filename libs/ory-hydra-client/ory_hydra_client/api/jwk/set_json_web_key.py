from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from typing import Dict
from ...models.json_web_key import JsonWebKey
from typing import cast



def _get_kwargs(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JsonWebKey,

) -> Dict[str, Any]:
    url = "{}/admin/keys/{set}/{kid}".format(
        _client.base_url,set=set_,kid=kid)

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[JsonWebKey]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JsonWebKey.from_dict(response.json())



        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[JsonWebKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JsonWebKey,

) -> Response[JsonWebKey]:
    """Set JSON Web Key

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):
        json_body (JsonWebKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKey]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
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
    kid: str,
    *,
    _client: Client,
    json_body: JsonWebKey,

) -> Optional[JsonWebKey]:
    """Set JSON Web Key

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):
        json_body (JsonWebKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKey]
    """


    return sync_detailed(
        set_=set_,
kid=kid,
_client=_client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JsonWebKey,

) -> Response[JsonWebKey]:
    """Set JSON Web Key

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):
        json_body (JsonWebKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKey]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
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
    kid: str,
    *,
    _client: Client,
    json_body: JsonWebKey,

) -> Optional[JsonWebKey]:
    """Set JSON Web Key

     Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your
    own.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):
        json_body (JsonWebKey):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonWebKey]
    """


    return (await asyncio_detailed(
        set_=set_,
kid=kid,
_client=_client,
json_body=json_body,

    )).parsed

