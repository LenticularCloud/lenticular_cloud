from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import Dict
from typing import Union
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List
import datetime




T = TypeVar("T", bound="AcceptConsentRequest")

@attr.s(auto_attribs=True)
class AcceptConsentRequest:
    """
    Attributes:
        grant_access_token_audience (Union[Unset, List[str]]):
        grant_scope (Union[Unset, List[str]]):
        handled_at (Union[Unset, datetime.datetime]):
        remember (Union[Unset, bool]): Remember, if set to true, tells ORY Hydra to remember this consent authorization
            and reuse it if the same
            client asks the same user for the same, or a subset of, scope.
        remember_for (Union[Unset, int]): RememberFor sets how long the consent authorization should be remembered for
            in seconds. If set to `0`, the
            authorization will be remembered indefinitely.
        session (Union[Unset, ConsentRequestSession]):
    """

    grant_access_token_audience: Union[Unset, List[str]] = UNSET
    grant_scope: Union[Unset, List[str]] = UNSET
    handled_at: Union[Unset, datetime.datetime] = UNSET
    remember: Union[Unset, bool] = UNSET
    remember_for: Union[Unset, int] = UNSET
    session: Union[Unset, 'ConsentRequestSession'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
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
        _d = src_dict.copy()
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
        session: Union[Unset, ConsentRequestSession]
        if isinstance(_session,  Unset):
            session = UNSET
        else:
            session = ConsentRequestSession.from_dict(_session)




        accept_consent_request = cls(
            grant_access_token_audience=grant_access_token_audience,
            grant_scope=grant_scope,
            handled_at=handled_at,
            remember=remember,
            remember_for=remember_for,
            session=session,
        )

        accept_consent_request.additional_properties = _d
        return accept_consent_request

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
