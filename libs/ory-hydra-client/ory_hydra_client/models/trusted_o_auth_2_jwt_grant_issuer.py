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
  from ..models.trusted_o_auth_2_jwt_grant_json_web_key import TrustedOAuth2JwtGrantJsonWebKey




T = TypeVar("T", bound="TrustedOAuth2JwtGrantIssuer")

@attr.s(auto_attribs=True)
class TrustedOAuth2JwtGrantIssuer:
    """OAuth2 JWT Bearer Grant Type Issuer Trust Relationship

    Attributes:
        allow_any_subject (Union[Unset, bool]): The "allow_any_subject" indicates that the issuer is allowed to have any
            principal as the subject of the JWT.
        created_at (Union[Unset, datetime.datetime]): The "created_at" indicates, when grant was created.
        expires_at (Union[Unset, datetime.datetime]): The "expires_at" indicates, when grant will expire, so we will
            reject assertion from "issuer" targeting "subject".
        id (Union[Unset, str]):  Example: 9edc811f-4e28-453c-9b46-4de65f00217f.
        issuer (Union[Unset, str]): The "issuer" identifies the principal that issued the JWT assertion (same as "iss"
            claim in JWT). Example: https://jwt-idp.example.com.
        public_key (Union[Unset, TrustedOAuth2JwtGrantJsonWebKey]): OAuth2 JWT Bearer Grant Type Issuer Trusted JSON Web
            Key
        scope (Union[Unset, List[str]]): The "scope" contains list of scope values (as described in Section 3.3 of OAuth
            2.0 [RFC6749]) Example: ['openid', 'offline'].
        subject (Union[Unset, str]): The "subject" identifies the principal that is the subject of the JWT. Example:
            mike@example.com.
    """

    allow_any_subject: Union[Unset, bool] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    expires_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    issuer: Union[Unset, str] = UNSET
    public_key: Union[Unset, 'TrustedOAuth2JwtGrantJsonWebKey'] = UNSET
    scope: Union[Unset, List[str]] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.trusted_o_auth_2_jwt_grant_json_web_key import TrustedOAuth2JwtGrantJsonWebKey
        allow_any_subject = self.allow_any_subject
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        expires_at: Union[Unset, str] = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        id = self.id
        issuer = self.issuer
        public_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_key, Unset):
            public_key = self.public_key.to_dict()

        scope: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope




        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_any_subject is not UNSET:
            field_dict["allow_any_subject"] = allow_any_subject
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if issuer is not UNSET:
            field_dict["issuer"] = issuer
        if public_key is not UNSET:
            field_dict["public_key"] = public_key
        if scope is not UNSET:
            field_dict["scope"] = scope
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.trusted_o_auth_2_jwt_grant_json_web_key import TrustedOAuth2JwtGrantJsonWebKey
        _d = src_dict.copy()
        allow_any_subject = _d.pop("allow_any_subject", UNSET)

        _created_at = _d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _expires_at = _d.pop("expires_at", UNSET)
        expires_at: Union[Unset, datetime.datetime]
        if isinstance(_expires_at,  Unset):
            expires_at = UNSET
        else:
            expires_at = isoparse(_expires_at)




        id = _d.pop("id", UNSET)

        issuer = _d.pop("issuer", UNSET)

        _public_key = _d.pop("public_key", UNSET)
        public_key: Union[Unset, TrustedOAuth2JwtGrantJsonWebKey]
        if isinstance(_public_key,  Unset):
            public_key = UNSET
        else:
            public_key = TrustedOAuth2JwtGrantJsonWebKey.from_dict(_public_key)




        scope = cast(List[str], _d.pop("scope", UNSET))


        subject = _d.pop("subject", UNSET)

        trusted_o_auth_2_jwt_grant_issuer = cls(
            allow_any_subject=allow_any_subject,
            created_at=created_at,
            expires_at=expires_at,
            id=id,
            issuer=issuer,
            public_key=public_key,
            scope=scope,
            subject=subject,
        )

        trusted_o_auth_2_jwt_grant_issuer.additional_properties = _d
        return trusted_o_auth_2_jwt_grant_issuer

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
