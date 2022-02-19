from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.json_web_key_set import JSONWebKeySet
from ...models.json_web_key_set_generator_request import JsonWebKeySetGeneratorRequest
from ...types import Response


def _get_kwargs(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySetGeneratorRequest,
) -> Dict[str, Any]:
    url = "{}/keys/{set}".format(_client.base_url, set=set_)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, JSONWebKeySet]]:
    if response.status_code == 201:
        response_201 = JSONWebKeySet.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = GenericError.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GenericError.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = GenericError.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, JSONWebKeySet]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySetGeneratorRequest,
) -> Response[Union[GenericError, JSONWebKeySet]]:
    """Generate a New JSON Web Key

     This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies
    available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys
    (RS256, ECDSA). If the specified JSON Web Key Set does not exist, it will be created.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySetGeneratorRequest):

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
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

    return _build_response(response=response)


def sync(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySetGeneratorRequest,
) -> Optional[Union[GenericError, JSONWebKeySet]]:
    """Generate a New JSON Web Key

     This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies
    available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys
    (RS256, ECDSA). If the specified JSON Web Key Set does not exist, it will be created.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySetGeneratorRequest):

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
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
    json_body: JsonWebKeySetGeneratorRequest,
) -> Response[Union[GenericError, JSONWebKeySet]]:
    """Generate a New JSON Web Key

     This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies
    available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys
    (RS256, ECDSA). If the specified JSON Web Key Set does not exist, it will be created.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySetGeneratorRequest):

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    kwargs = _get_kwargs(
        set_=set_,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    set_: str,
    *,
    _client: Client,
    json_body: JsonWebKeySetGeneratorRequest,
) -> Optional[Union[GenericError, JSONWebKeySet]]:
    """Generate a New JSON Web Key

     This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies
    available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys
    (RS256, ECDSA). If the specified JSON Web Key Set does not exist, it will be created.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        json_body (JsonWebKeySetGeneratorRequest):

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """

    return (
        await asyncio_detailed(
            set_=set_,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
