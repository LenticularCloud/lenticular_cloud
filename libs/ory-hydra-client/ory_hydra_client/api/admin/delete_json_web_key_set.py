from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.generic_error import GenericError
from ...types import Response


def _get_kwargs(
    set_: str,
    *,
    _client: Client,
) -> Dict[str, Any]:
    url = "{}/keys/{set}".format(_client.base_url, set=set_)

    headers: Dict[str, str] = _client.get_headers()
    cookies: Dict[str, Any] = _client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": _client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GenericError]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GenericError]]:
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
) -> Response[Union[Any, GenericError]]:
    """Delete a JSON Web Key Set

     Use this endpoint to delete a complete JSON Web Key Set and all the keys in that set.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        set_=set_,
        _client=_client,
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
) -> Optional[Union[Any, GenericError]]:
    """Delete a JSON Web Key Set

     Use this endpoint to delete a complete JSON Web Key Set and all the keys in that set.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return sync_detailed(
        set_=set_,
        _client=_client,
    ).parsed


async def asyncio_detailed(
    set_: str,
    *,
    _client: Client,
) -> Response[Union[Any, GenericError]]:
    """Delete a JSON Web Key Set

     Use this endpoint to delete a complete JSON Web Key Set and all the keys in that set.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):

    Returns:
        Response[Union[Any, GenericError]]
    """

    kwargs = _get_kwargs(
        set_=set_,
        _client=_client,
    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    set_: str,
    *,
    _client: Client,
) -> Optional[Union[Any, GenericError]]:
    """Delete a JSON Web Key Set

     Use this endpoint to delete a complete JSON Web Key Set and all the keys in that set.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):

    Returns:
        Response[Union[Any, GenericError]]
    """

    return (
        await asyncio_detailed(
            set_=set_,
            _client=_client,
        )
    ).parsed
