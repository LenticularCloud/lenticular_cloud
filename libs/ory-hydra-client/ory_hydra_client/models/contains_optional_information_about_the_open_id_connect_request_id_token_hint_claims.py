from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset






T = TypeVar("T", bound="ContainsOptionalInformationAboutTheOpenIDConnectRequestIdTokenHintClaims")

@attr.s(auto_attribs=True)
class ContainsOptionalInformationAboutTheOpenIDConnectRequestIdTokenHintClaims:
    """IDTokenHintClaims are the claims of the ID Token previously issued by the Authorization Server being passed as a
hint about the
End-User's current or past authenticated session with the Client.

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        contains_optional_information_about_the_open_id_connect_request_id_token_hint_claims = cls(
        )

        contains_optional_information_about_the_open_id_connect_request_id_token_hint_claims.additional_properties = _d
        return contains_optional_information_about_the_open_id_connect_request_id_token_hint_claims

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
