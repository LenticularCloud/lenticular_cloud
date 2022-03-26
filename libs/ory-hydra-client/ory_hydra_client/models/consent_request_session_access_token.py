from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ConsentRequestSessionAccessToken")


@attr.s(auto_attribs=True)
class ConsentRequestSessionAccessToken:
    """AccessToken sets session data for the access and refresh token, as well as any future tokens issued by the
    refresh grant. Keep in mind that this data will be available to anyone performing OAuth 2.0 Challenge Introspection.
    If only your services can perform OAuth 2.0 Challenge Introspection, this is usually fine. But if third parties
    can access that endpoint as well, sensitive data from the session might be exposed to them. Use with care!

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        consent_request_session_access_token = cls()

        consent_request_session_access_token.additional_properties = _d
        return consent_request_session_access_token

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