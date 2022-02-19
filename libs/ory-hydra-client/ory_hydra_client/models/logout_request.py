from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogoutRequest")


@attr.s(auto_attribs=True)
class LogoutRequest:
    """
    Attributes:
        request_url (Union[Unset, str]): RequestURL is the original Logout URL requested.
        rp_initiated (Union[Unset, bool]): RPInitiated is set to true if the request was initiated by a Relying Party
            (RP), also known as an OAuth 2.0 Client.
        sid (Union[Unset, str]): SessionID is the login session ID that was requested to log out.
        subject (Union[Unset, str]): Subject is the user for whom the logout was request.
    """

    request_url: Union[Unset, str] = UNSET
    rp_initiated: Union[Unset, bool] = UNSET
    sid: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        request_url = self.request_url
        rp_initiated = self.rp_initiated
        sid = self.sid
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if request_url is not UNSET:
            field_dict["request_url"] = request_url
        if rp_initiated is not UNSET:
            field_dict["rp_initiated"] = rp_initiated
        if sid is not UNSET:
            field_dict["sid"] = sid
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        request_url = _d.pop("request_url", UNSET)

        rp_initiated = _d.pop("rp_initiated", UNSET)

        sid = _d.pop("sid", UNSET)

        subject = _d.pop("subject", UNSET)

        logout_request = cls(
            request_url=request_url,
            rp_initiated=rp_initiated,
            sid=sid,
            subject=subject,
        )

        logout_request.additional_properties = _d
        return logout_request

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
