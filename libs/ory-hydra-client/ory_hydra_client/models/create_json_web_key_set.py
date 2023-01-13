from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateJsonWebKeySet")

@attr.s(auto_attribs=True)
class CreateJsonWebKeySet:
    """Create JSON Web Key Set Request Body

    Attributes:
        alg (str): JSON Web Key Algorithm

            The algorithm to be used for creating the key. Supports `RS256`, `ES256`, `ES512`, `HS512`, and `HS256`.
        kid (str): JSON Web Key ID

            The Key ID of the key to be created.
        use (str): JSON Web Key Use

            The "use" (public key use) parameter identifies the intended use of
            the public key. The "use" parameter is employed to indicate whether
            a public key is used for encrypting data or verifying the signature
            on data. Valid values are "enc" and "sig".
    """

    alg: str
    kid: str
    use: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        alg = self.alg
        kid = self.kid
        use = self.use

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "alg": alg,
            "kid": kid,
            "use": use,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        alg = _d.pop("alg")

        kid = _d.pop("kid")

        use = _d.pop("use")

        create_json_web_key_set = cls(
            alg=alg,
            kid=kid,
            use=use,
        )

        create_json_web_key_set.additional_properties = _d
        return create_json_web_key_set

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
