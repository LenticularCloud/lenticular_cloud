from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="TrustedOAuth2JwtGrantJsonWebKey")

@attr.s(auto_attribs=True)
class TrustedOAuth2JwtGrantJsonWebKey:
    """OAuth2 JWT Bearer Grant Type Issuer Trusted JSON Web Key

    Attributes:
        kid (Union[Unset, str]): The "key_id" is key unique identifier (same as kid header in jws/jwt). Example:
            123e4567-e89b-12d3-a456-426655440000.
        set_ (Union[Unset, str]): The "set" is basically a name for a group(set) of keys. Will be the same as "issuer"
            in grant. Example: https://jwt-idp.example.com.
    """

    kid: Union[Unset, str] = UNSET
    set_: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        kid = self.kid
        set_ = self.set_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kid is not UNSET:
            field_dict["kid"] = kid
        if set_ is not UNSET:
            field_dict["set"] = set_

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        kid = _d.pop("kid", UNSET)

        set_ = _d.pop("set", UNSET)

        trusted_o_auth_2_jwt_grant_json_web_key = cls(
            kid=kid,
            set_=set_,
        )

        trusted_o_auth_2_jwt_grant_json_web_key.additional_properties = _d
        return trusted_o_auth_2_jwt_grant_json_web_key

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
