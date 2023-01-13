from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union




T = TypeVar("T", bound="IntrospectOAuth2TokenData")

@attr.s(auto_attribs=True)
class IntrospectOAuth2TokenData:
    """
    Attributes:
        token (str): The string value of the token. For access tokens, this
            is the "access_token" value returned from the token endpoint
            defined in OAuth 2.0. For refresh tokens, this is the "refresh_token"
            value returned.
        scope (Union[Unset, str]): An optional, space separated list of required scopes. If the access token was not
            granted one of the
            scopes, the result of active will be false.
    """

    token: str
    scope: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        scope = self.scope

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "token": token,
        })
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        token = _d.pop("token")

        scope = _d.pop("scope", UNSET)

        introspect_o_auth_2_token_data = cls(
            token=token,
            scope=scope,
        )

        introspect_o_auth_2_token_data.additional_properties = _d
        return introspect_o_auth_2_token_data

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
