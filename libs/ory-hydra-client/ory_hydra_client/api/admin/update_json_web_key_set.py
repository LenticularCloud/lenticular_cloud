from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET

from ...models.generic_error import GenericError
from typing import Dict
from typing import cast
from ...models.json_web_key_set import JSONWebKeySet



def _get_kwargs(
    set_: str,
    *,
    _client: Client,
    json_body: JSONWebKeySet,

) -> Dict[str, Any]:
    url = "{}/keys/{set}".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[GenericError, JSONWebKeySet]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JSONWebKeySet.from_dict(response.json())



        return response_200
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
    json_body: JSONWebKeySet,

) -> Response[Union[GenericError, JSONWebKeySet]]:
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
        json_body (JSONWebKeySet): It is important that this model object is named JSONWebKeySet
            for
            "swagger generate spec" to generate only on definition of a
            JSONWebKeySet. Since one with the same name is previously defined as
            client.Client.JSONWebKeys and this one is last, this one will be
            effectively written in the swagger spec.

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
    json_body: JSONWebKeySet,

) -> Optional[Union[GenericError, JSONWebKeySet]]:
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
        json_body (JSONWebKeySet): It is important that this model object is named JSONWebKeySet
            for
            "swagger generate spec" to generate only on definition of a
            JSONWebKeySet. Since one with the same name is previously defined as
            client.Client.JSONWebKeys and this one is last, this one will be
            effectively written in the swagger spec.

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
    json_body: JSONWebKeySet,

) -> Response[Union[GenericError, JSONWebKeySet]]:
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
        json_body (JSONWebKeySet): It is important that this model object is named JSONWebKeySet
            for
            "swagger generate spec" to generate only on definition of a
            JSONWebKeySet. Since one with the same name is previously defined as
            client.Client.JSONWebKeys and this one is last, this one will be
            effectively written in the swagger spec.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
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

    return _build_response(response=response)

async def asyncio(
    set_: str,
    *,
    _client: Client,
    json_body: JSONWebKeySet,

) -> Optional[Union[GenericError, JSONWebKeySet]]:
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
        json_body (JSONWebKeySet): It is important that this model object is named JSONWebKeySet
            for
            "swagger generate spec" to generate only on definition of a
            JSONWebKeySet. Since one with the same name is previously defined as
            client.Client.JSONWebKeys and this one is last, this one will be
            effectively written in the swagger spec.

    Returns:
        Response[Union[GenericError, JSONWebKeySet]]
    """


    return (await asyncio_detailed(
        set_=set_,
_client=_client,
json_body=json_body,

    )).parsed

