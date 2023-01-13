from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from typing import Dict
from dateutil.parser import isoparse
import datetime
from typing import cast, List

if TYPE_CHECKING:
  from ..models.json_web_key import JsonWebKey




T = TypeVar("T", bound="TrustOAuth2JwtGrantIssuer")

@attr.s(auto_attribs=True)
class TrustOAuth2JwtGrantIssuer:
    """Trust OAuth2 JWT Bearer Grant Type Issuer Request Body

    Attributes:
        expires_at (datetime.datetime): The "expires_at" indicates, when grant will expire, so we will reject assertion
            from "issuer" targeting "subject".
        issuer (str): The "issuer" identifies the principal that issued the JWT assertion (same as "iss" claim in JWT).
            Example: https://jwt-idp.example.com.
        jwk (JsonWebKey):
        scope (List[str]): The "scope" contains list of scope values (as described in Section 3.3 of OAuth 2.0
            [RFC6749]) Example: ['openid', 'offline'].
        allow_any_subject (Union[Unset, bool]): The "allow_any_subject" indicates that the issuer is allowed to have any
            principal as the subject of the JWT.
        subject (Union[Unset, str]): The "subject" identifies the principal that is the subject of the JWT. Example:
            mike@example.com.
    """

    expires_at: datetime.datetime
    issuer: str
    jwk: 'JsonWebKey'
    scope: List[str]
    allow_any_subject: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.json_web_key import JsonWebKey
        expires_at = self.expires_at.isoformat()

        issuer = self.issuer
        jwk = self.jwk.to_dict()

        scope = self.scope




        allow_any_subject = self.allow_any_subject
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "expires_at": expires_at,
            "issuer": issuer,
            "jwk": jwk,
            "scope": scope,
        })
        if allow_any_subject is not UNSET:
            field_dict["allow_any_subject"] = allow_any_subject
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_web_key import JsonWebKey
        _d = src_dict.copy()
        expires_at = isoparse(_d.pop("expires_at"))




        issuer = _d.pop("issuer")

        jwk = JsonWebKey.from_dict(_d.pop("jwk"))




        scope = cast(List[str], _d.pop("scope"))


        allow_any_subject = _d.pop("allow_any_subject", UNSET)

        subject = _d.pop("subject", UNSET)

        trust_o_auth_2_jwt_grant_issuer = cls(
            expires_at=expires_at,
            issuer=issuer,
            jwk=jwk,
            scope=scope,
            allow_any_subject=allow_any_subject,
            subject=subject,
        )

        trust_o_auth_2_jwt_grant_issuer.additional_properties = _d
        return trust_o_auth_2_jwt_grant_issuer

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
