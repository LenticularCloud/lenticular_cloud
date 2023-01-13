from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from typing import cast
from typing import Dict



def _get_kwargs(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Dict[str, Any]:
    url = "{}/keys/{set}/{kid}".format(
        _client.base_url,set=set_,kid=kid)

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
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = GenericError.from_dict(response.json())



        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = GenericError.from_dict(response.json())



        return response_403
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
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
    kid: str,
    *,
    _client: Client,

) -> Response[Union[Any, GenericError]]:
    """Delete a JSON Web Key

     Use this endpoint to delete a single JSON Web Key.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
_client=_client,

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

) -> Optional[Union[Any, GenericError]]:
    """Delete a JSON Web Key

     Use this endpoint to delete a single JSON Web Key.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return sync_detailed(
        set_=set_,
kid=kid,
_client=_client,

    ).parsed

async def asyncio_detailed(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Response[Union[Any, GenericError]]:
    """Delete a JSON Web Key

     Use this endpoint to delete a single JSON Web Key.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    kwargs = _get_kwargs(
        set_=set_,
kid=kid,
_client=_client,

    )

    async with httpx.AsyncClient(verify=_client.verify_ssl) as __client:
        response = await __client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    set_: str,
    kid: str,
    *,
    _client: Client,

) -> Optional[Union[Any, GenericError]]:
    """Delete a JSON Web Key

     Use this endpoint to delete a single JSON Web Key.

    A JSON Web Key (JWK) is a JavaScript Object Notation (JSON) data structure that represents a
    cryptographic key. A JWK Set is a JSON data structure that represents a set of JWKs. A JSON Web Key
    is identified by its set and key id. ORY Hydra uses this functionality to store cryptographic keys
    used for TLS and JSON Web Tokens (such as OpenID Connect ID tokens), and allows storing user-defined
    keys as well.

    Args:
        set_ (str):
        kid (str):

    Returns:
        Response[Union[Any, GenericError]]
    """


    return (await asyncio_detailed(
        set_=set_,
kid=kid,
_client=_client,

    )).parsed

