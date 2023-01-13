from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import Dict
from dateutil.parser import isoparse
import datetime
from typing import cast, List

if TYPE_CHECKING:
  from ..models.pass_session_data_to_a_consent_request import PassSessionDataToAConsentRequest
  from ..models.o_auth_20_consent_session_expires_at import OAuth20ConsentSessionExpiresAt
  from ..models.contains_information_on_an_ongoing_consent_request import ContainsInformationOnAnOngoingConsentRequest




T = TypeVar("T", bound="OAuth20ConsentSession")

@attr.s(auto_attribs=True)
class OAuth20ConsentSession:
    """A completed OAuth 2.0 Consent Session.

    Attributes:
        consent_request (Union[Unset, ContainsInformationOnAnOngoingConsentRequest]):
        expires_at (Union[Unset, OAuth20ConsentSessionExpiresAt]):
        grant_access_token_audience (Union[Unset, List[str]]):
        grant_scope (Union[Unset, List[str]]):
        handled_at (Union[Unset, datetime.datetime]):
        remember (Union[Unset, bool]): Remember Consent

            Remember, if set to true, tells ORY Hydra to remember this consent authorization and reuse it if the same
            client asks the same user for the same, or a subset of, scope.
        remember_for (Union[Unset, int]): Remember Consent For

            RememberFor sets how long the consent authorization should be remembered for in seconds. If set to `0`, the
            authorization will be remembered indefinitely.
        session (Union[Unset, PassSessionDataToAConsentRequest]):
    """

    consent_request: Union[Unset, 'ContainsInformationOnAnOngoingConsentRequest'] = UNSET
    expires_at: Union[Unset, 'OAuth20ConsentSessionExpiresAt'] = UNSET
    grant_access_token_audience: Union[Unset, List[str]] = UNSET
    grant_scope: Union[Unset, List[str]] = UNSET
    handled_at: Union[Unset, datetime.datetime] = UNSET
    remember: Union[Unset, bool] = UNSET
    remember_for: Union[Unset, int] = UNSET
    session: Union[Unset, 'PassSessionDataToAConsentRequest'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.pass_session_data_to_a_consent_request import PassSessionDataToAConsentRequest
        from ..models.o_auth_20_consent_session_expires_at import OAuth20ConsentSessionExpiresAt
        from ..models.contains_information_on_an_ongoing_consent_request import ContainsInformationOnAnOngoingConsentRequest
        consent_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.consent_request, Unset):
            consent_request = self.consent_request.to_dict()

        expires_at: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.to_dict()

        grant_access_token_audience: Union[Unset, List[str]] = UNSET
        if not isinstance(self.grant_access_token_audience, Unset):
            grant_access_token_audience = self.grant_access_token_audience




        grant_scope: Union[Unset, List[str]] = UNSET
        if not isinstance(self.grant_scope, Unset):
            grant_scope = self.grant_scope




        handled_at: Union[Unset, str] = UNSET
        if not isinstance(self.handled_at, Unset):
            handled_at = self.handled_at.isoformat()

        remember = self.remember
        remember_for = self.remember_for
        session: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.session, Unset):
            session = self.session.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if consent_request is not UNSET:
            field_dict["consent_request"] = consent_request
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if grant_access_token_audience is not UNSET:
            field_dict["grant_access_token_audience"] = grant_access_token_audience
        if grant_scope is not UNSET:
            field_dict["grant_scope"] = grant_scope
        if handled_at is not UNSET:
            field_dict["handled_at"] = handled_at
        if remember is not UNSET:
            field_dict["remember"] = remember
        if remember_for is not UNSET:
            field_dict["remember_for"] = remember_for
        if session is not UNSET:
            field_dict["session"] = session

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pass_session_data_to_a_consent_request import PassSessionDataToAConsentRequest
        from ..models.o_auth_20_consent_session_expires_at import OAuth20ConsentSessionExpiresAt
        from ..models.contains_information_on_an_ongoing_consent_request import ContainsInformationOnAnOngoingConsentRequest
        _d = src_dict.copy()
        _consent_request = _d.pop("consent_request", UNSET)
        consent_request: Union[Unset, ContainsInformationOnAnOngoingConsentRequest]
        if isinstance(_consent_request,  Unset):
            consent_request = UNSET
        else:
            consent_request = ContainsInformationOnAnOngoingConsentRequest.from_dict(_consent_request)




        _expires_at = _d.pop("expires_at", UNSET)
        expires_at: Union[Unset, OAuth20ConsentSessionExpiresAt]
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = OAuth20ConsentSessionExpiresAt.from_dict(_expires_at)




        grant_access_token_audience = cast(List[str], _d.pop("grant_access_token_audience", UNSET))


        grant_scope = cast(List[str], _d.pop("grant_scope", UNSET))


        _handled_at = _d.pop("handled_at", UNSET)
        handled_at: Union[Unset, datetime.datetime]
        if isinstance(_handled_at,  Unset):
            handled_at = UNSET
        else:
            handled_at = isoparse(_handled_at)




        remember = _d.pop("remember", UNSET)

        remember_for = _d.pop("remember_for", UNSET)

        _session = _d.pop("session", UNSET)
        session: Union[Unset, PassSessionDataToAConsentRequest]
        if isinstance(_session,  Unset):
            session = UNSET
        else:
            session = PassSessionDataToAConsentRequest.from_dict(_session)




        o_auth_20_consent_session = cls(
            consent_request=consent_request,
            expires_at=expires_at,
            grant_access_token_audience=grant_access_token_audience,
            grant_scope=grant_scope,
            handled_at=handled_at,
            remember=remember,
            remember_for=remember_for,
            session=session,
        )

        o_auth_20_consent_session.additional_properties = _d
        return o_auth_20_consent_session

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
