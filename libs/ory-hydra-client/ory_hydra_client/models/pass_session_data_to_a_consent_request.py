from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="PassSessionDataToAConsentRequest")

@attr.s(auto_attribs=True)
class PassSessionDataToAConsentRequest:
    """
    Attributes:
        access_token (Union[Unset, Any]): AccessToken sets session data for the access and refresh token, as well as any
            future tokens issued by the
            refresh grant. Keep in mind that this data will be available to anyone performing OAuth 2.0 Challenge
            Introspection.
            If only your services can perform OAuth 2.0 Challenge Introspection, this is usually fine. But if third parties
            can access that endpoint as well, sensitive data from the session might be exposed to them. Use with care!
        id_token (Union[Unset, Any]): IDToken sets session data for the OpenID Connect ID token. Keep in mind that the
            session'id payloads are readable
            by anyone that has access to the ID Challenge. Use with care!
    """

    access_token: Union[Unset, Any] = UNSET
    id_token: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        access_token = self.access_token
        id_token = self.id_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if id_token is not UNSET:
            field_dict["id_token"] = id_token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        access_token = _d.pop("access_token", UNSET)

        id_token = _d.pop("id_token", UNSET)

        pass_session_data_to_a_consent_request = cls(
            access_token=access_token,
            id_token=id_token,
        )

        pass_session_data_to_a_consent_request.additional_properties = _d
        return pass_session_data_to_a_consent_request

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
