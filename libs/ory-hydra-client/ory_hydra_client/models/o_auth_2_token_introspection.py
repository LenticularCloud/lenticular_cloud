from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.o_auth_2_token_introspection_ext import OAuth2TokenIntrospectionExt
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuth2TokenIntrospection")


@attr.s(auto_attribs=True)
class OAuth2TokenIntrospection:
    """https://tools.ietf.org/html/rfc7662

    Attributes:
        active (bool): Active is a boolean indicator of whether or not the presented token
            is currently active.  The specifics of a token's "active" state
            will vary depending on the implementation of the authorization
            server and the information it keeps about its tokens, but a "true"
            value return for the "active" property will generally indicate
            that a given token has been issued by this authorization server,
            has not been revoked by the resource owner, and is within its
            given time window of validity (e.g., after its issuance time and
            before its expiration time).
        aud (Union[Unset, List[str]]): Audience contains a list of the token's intended audiences.
        client_id (Union[Unset, str]): ID is aclient identifier for the OAuth 2.0 client that
            requested this token.
        exp (Union[Unset, int]): Expires at is an integer timestamp, measured in the number of seconds
            since January 1 1970 UTC, indicating when this token will expire.
        ext (Union[Unset, OAuth2TokenIntrospectionExt]): Extra is arbitrary data set by the session.
        iat (Union[Unset, int]): Issued at is an integer timestamp, measured in the number of seconds
            since January 1 1970 UTC, indicating when this token was
            originally issued.
        iss (Union[Unset, str]): IssuerURL is a string representing the issuer of this token
        nbf (Union[Unset, int]): NotBefore is an integer timestamp, measured in the number of seconds
            since January 1 1970 UTC, indicating when this token is not to be
            used before.
        obfuscated_subject (Union[Unset, str]): ObfuscatedSubject is set when the subject identifier algorithm was set
            to "pairwise" during authorization.
            It is the `sub` value of the ID Token that was issued.
        scope (Union[Unset, str]): Scope is a JSON string containing a space-separated list of
            scopes associated with this token.
        sub (Union[Unset, str]): Subject of the token, as defined in JWT [RFC7519].
            Usually a machine-readable identifier of the resource owner who
            authorized this token.
        token_type (Union[Unset, str]): TokenType is the introspected token's type, typically `Bearer`.
        token_use (Union[Unset, str]): TokenUse is the introspected token's use, for example `access_token` or
            `refresh_token`.
        username (Union[Unset, str]): Username is a human-readable identifier for the resource owner who
            authorized this token.
    """

    active: bool
    aud: Union[Unset, List[str]] = UNSET
    client_id: Union[Unset, str] = UNSET
    exp: Union[Unset, int] = UNSET
    ext: Union[Unset, OAuth2TokenIntrospectionExt] = UNSET
    iat: Union[Unset, int] = UNSET
    iss: Union[Unset, str] = UNSET
    nbf: Union[Unset, int] = UNSET
    obfuscated_subject: Union[Unset, str] = UNSET
    scope: Union[Unset, str] = UNSET
    sub: Union[Unset, str] = UNSET
    token_type: Union[Unset, str] = UNSET
    token_use: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        aud: Union[Unset, List[str]] = UNSET
        if not isinstance(self.aud, Unset):
            aud = self.aud

        client_id = self.client_id
        exp = self.exp
        ext: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ext, Unset):
            ext = self.ext.to_dict()

        iat = self.iat
        iss = self.iss
        nbf = self.nbf
        obfuscated_subject = self.obfuscated_subject
        scope = self.scope
        sub = self.sub
        token_type = self.token_type
        token_use = self.token_use
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "active": active,
            }
        )
        if aud is not UNSET:
            field_dict["aud"] = aud
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if exp is not UNSET:
            field_dict["exp"] = exp
        if ext is not UNSET:
            field_dict["ext"] = ext
        if iat is not UNSET:
            field_dict["iat"] = iat
        if iss is not UNSET:
            field_dict["iss"] = iss
        if nbf is not UNSET:
            field_dict["nbf"] = nbf
        if obfuscated_subject is not UNSET:
            field_dict["obfuscated_subject"] = obfuscated_subject
        if scope is not UNSET:
            field_dict["scope"] = scope
        if sub is not UNSET:
            field_dict["sub"] = sub
        if token_type is not UNSET:
            field_dict["token_type"] = token_type
        if token_use is not UNSET:
            field_dict["token_use"] = token_use
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        active = _d.pop("active")

        aud = cast(List[str], _d.pop("aud", UNSET))

        client_id = _d.pop("client_id", UNSET)

        exp = _d.pop("exp", UNSET)

        _ext = _d.pop("ext", UNSET)
        ext: Union[Unset, OAuth2TokenIntrospectionExt]
        if isinstance(_ext, Unset):
            ext = UNSET
        else:
            ext = OAuth2TokenIntrospectionExt.from_dict(_ext)

        iat = _d.pop("iat", UNSET)

        iss = _d.pop("iss", UNSET)

        nbf = _d.pop("nbf", UNSET)

        obfuscated_subject = _d.pop("obfuscated_subject", UNSET)

        scope = _d.pop("scope", UNSET)

        sub = _d.pop("sub", UNSET)

        token_type = _d.pop("token_type", UNSET)

        token_use = _d.pop("token_use", UNSET)

        username = _d.pop("username", UNSET)

        o_auth_2_token_introspection = cls(
            active=active,
            aud=aud,
            client_id=client_id,
            exp=exp,
            ext=ext,
            iat=iat,
            iss=iss,
            nbf=nbf,
            obfuscated_subject=obfuscated_subject,
            scope=scope,
            sub=sub,
            token_type=token_type,
            token_use=token_use,
            username=username,
        )

        o_auth_2_token_introspection.additional_properties = _d
        return o_auth_2_token_introspection

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
