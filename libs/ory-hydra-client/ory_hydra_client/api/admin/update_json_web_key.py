from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...models.json_web_key import JSONWebKey
from ...types import Response


def _get_kwargs(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JSONWebKey,
) -> Dict[str, Any]:
    url = "{}/keys/{set}/{kid}".format(_client.base_url, set=set_, kid=kid)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, JSONWebKey]]:
    if response.status_code == 200:
        response_200 = JSONWebKey.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[GenericError, JSONWebKey]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JSONWebKey,
) -> Response[Union[GenericError, JSONWebKey]]:
    """Update a JSON Web Key

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
        json_body (JSONWebKey): It is important that this model object is named JSONWebKey for
            "swagger generate spec" to generate only on definition of a
            JSONWebKey.

    Returns:
        Response[Union[GenericError, JSONWebKey]]
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

    return _build_response(response=response)


def sync(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JSONWebKey,
) -> Optional[Union[GenericError, JSONWebKey]]:
    """Update a JSON Web Key

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
        json_body (JSONWebKey): It is important that this model object is named JSONWebKey for
            "swagger generate spec" to generate only on definition of a
            JSONWebKey.

    Returns:
        Response[Union[GenericError, JSONWebKey]]
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
    json_body: JSONWebKey,
) -> Response[Union[GenericError, JSONWebKey]]:
    """Update a JSON Web Key

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
        json_body (JSONWebKey): It is important that this model object is named JSONWebKey for
            "swagger generate spec" to generate only on definition of a
            JSONWebKey.

    Returns:
        Response[Union[GenericError, JSONWebKey]]
    """

    kwargs = _get_kwargs(
        set_=set_,
        kid=kid,
        _client=_client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    set_: str,
    kid: str,
    *,
    _client: Client,
    json_body: JSONWebKey,
) -> Optional[Union[GenericError, JSONWebKey]]:
    """Update a JSON Web Key

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
        json_body (JSONWebKey): It is important that this model object is named JSONWebKey for
            "swagger generate spec" to generate only on definition of a
            JSONWebKey.

    Returns:
        Response[Union[GenericError, JSONWebKey]]
    """

    return (
        await asyncio_detailed(
            set_=set_,
            kid=kid,
            _client=_client,
            json_body=json_body,
        )
    ).parsed
