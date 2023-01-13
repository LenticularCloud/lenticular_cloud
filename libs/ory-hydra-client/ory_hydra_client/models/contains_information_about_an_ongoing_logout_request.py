from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from ..types import UNSET, Unset
from typing import Dict
from typing import Union

if TYPE_CHECKING:
  from ..models.o_auth_20_client import OAuth20Client




T = TypeVar("T", bound="ContainsInformationAboutAnOngoingLogoutRequest")

@attr.s(auto_attribs=True)
class ContainsInformationAboutAnOngoingLogoutRequest:
    """
    Attributes:
        challenge (Union[Unset, str]): Challenge is the identifier ("logout challenge") of the logout authentication
            request. It is used to
            identify the session.
        client (Union[Unset, OAuth20Client]): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID Connect flows.
            Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
        request_url (Union[Unset, str]): RequestURL is the original Logout URL requested.
        rp_initiated (Union[Unset, bool]): RPInitiated is set to true if the request was initiated by a Relying Party
            (RP), also known as an OAuth 2.0 Client.
        sid (Union[Unset, str]): SessionID is the login session ID that was requested to log out.
        subject (Union[Unset, str]): Subject is the user for whom the logout was request.
    """

    challenge: Union[Unset, str] = UNSET
    client: Union[Unset, 'OAuth20Client'] = UNSET
    request_url: Union[Unset, str] = UNSET
    rp_initiated: Union[Unset, bool] = UNSET
    sid: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.o_auth_20_client import OAuth20Client
        challenge = self.challenge
        client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        request_url = self.request_url
        rp_initiated = self.rp_initiated
        sid = self.sid
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if client is not UNSET:
            field_dict["client"] = client
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
        from ..models.o_auth_20_client import OAuth20Client
        _d = src_dict.copy()
        challenge = _d.pop("challenge", UNSET)

        _client = _d.pop("client", UNSET)
        client: Union[Unset, OAuth20Client]
        if isinstance(_client,  Unset):
            client = UNSET
        else:
            client = OAuth20Client.from_dict(_client)




        request_url = _d.pop("request_url", UNSET)

        rp_initiated = _d.pop("rp_initiated", UNSET)

        sid = _d.pop("sid", UNSET)

        subject = _d.pop("subject", UNSET)

        contains_information_about_an_ongoing_logout_request = cls(
            challenge=challenge,
            client=client,
            request_url=request_url,
            rp_initiated=rp_initiated,
            sid=sid,
            subject=subject,
        )

        contains_information_about_an_ongoing_logout_request.additional_properties = _d
        return contains_information_about_an_ongoing_logout_request

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
