from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="OAuth2TokenExchange")

@attr.s(auto_attribs=True)
class OAuth2TokenExchange:
    """OAuth2 Token Exchange Result

    Attributes:
        access_token (Union[Unset, str]): The access token issued by the authorization server.
        expires_in (Union[Unset, int]): The lifetime in seconds of the access token. For
            example, the value "3600" denotes that the access token will
            expire in one hour from the time the response was generated.
        id_token (Union[Unset, int]): To retrieve a refresh token request the id_token scope.
        refresh_token (Union[Unset, str]): The refresh token, which can be used to obtain new
            access tokens. To retrieve it add the scope "offline" to your access token request.
        scope (Union[Unset, str]): The scope of the access token
        token_type (Union[Unset, str]): The type of the token issued
    """

    access_token: Union[Unset, str] = UNSET
    expires_in: Union[Unset, int] = UNSET
    id_token: Union[Unset, int] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        expires_in = self.expires_in
        id_token = self.id_token
        refresh_token = self.refresh_token
        scope = self.scope
        token_type = self.token_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if expires_in is not UNSET:
            field_dict["expires_in"] = expires_in
        if id_token is not UNSET:
            field_dict["id_token"] = id_token
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if scope is not UNSET:
            field_dict["scope"] = scope
        if token_type is not UNSET:
            field_dict["token_type"] = token_type

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        access_token = _d.pop("access_token", UNSET)

        expires_in = _d.pop("expires_in", UNSET)

        id_token = _d.pop("id_token", UNSET)

        refresh_token = _d.pop("refresh_token", UNSET)

        scope = _d.pop("scope", UNSET)

        token_type = _d.pop("token_type", UNSET)

        o_auth_2_token_exchange = cls(
            access_token=access_token,
            expires_in=expires_in,
            id_token=id_token,
            refresh_token=refresh_token,
            scope=scope,
            token_type=token_type,
        )

        o_auth_2_token_exchange.additional_properties = _d
        return o_auth_2_token_exchange

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
