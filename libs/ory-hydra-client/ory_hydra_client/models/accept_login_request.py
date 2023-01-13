from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Union
from typing import cast
from ..types import UNSET, Unset
from typing import Dict




T = TypeVar("T", bound="AcceptLoginRequest")

@attr.s(auto_attribs=True)
class AcceptLoginRequest:
    """
    Attributes:
        subject (str): Subject is the user ID of the end-user that authenticated.
        acr (Union[Unset, str]): ACR sets the Authentication AuthorizationContext Class Reference value for this
            authentication session. You can use it
            to express that, for example, a user authenticated using two factor authentication.
        context (Union[Unset, JSONRawMessage]):
        force_subject_identifier (Union[Unset, str]): ForceSubjectIdentifier forces the "pairwise" user ID of the end-
            user that authenticated. The "pairwise" user ID refers to the
            (Pairwise Identifier Algorithm)[http://openid.net/specs/openid-connect-core-1_0.html#PairwiseAlg] of the OpenID
            Connect specification. It allows you to set an obfuscated subject ("user") identifier that is unique to the
            client.

            Please note that this changes the user ID on endpoint /userinfo and sub claim of the ID Token. It does not
            change the
            sub claim in the OAuth 2.0 Introspection.

            Per default, ORY Hydra handles this value with its own algorithm. In case you want to set this yourself
            you can use this field. Please note that setting this field has no effect if `pairwise` is not configured in
            ORY Hydra or the OAuth 2.0 Client does not expect a pairwise identifier (set via `subject_type` key in the
            client's
            configuration).

            Please also be aware that ORY Hydra is unable to properly compute this value during authentication. This implies
            that you have to compute this value on every authentication process (probably depending on the client ID or some
            other unique value).

            If you fail to compute the proper value, then authentication processes which have id_token_hint set might fail.
        remember (Union[Unset, bool]): Remember, if set to true, tells ORY Hydra to remember this user by telling the
            user agent (browser) to store
            a cookie with authentication data. If the same user performs another OAuth 2.0 Authorization Request, he/she
            will not be asked to log in again.
        remember_for (Union[Unset, int]): RememberFor sets how long the authentication should be remembered for in
            seconds. If set to `0`, the
            authorization will be remembered for the duration of the browser session (using a session cookie).
    """

    subject: str
    acr: Union[Unset, str] = UNSET
    context: Union[Unset, 'JSONRawMessage'] = UNSET
    force_subject_identifier: Union[Unset, str] = UNSET
    remember: Union[Unset, bool] = UNSET
    remember_for: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        subject = self.subject
        acr = self.acr
        context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        force_subject_identifier = self.force_subject_identifier
        remember = self.remember
        remember_for = self.remember_for

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "subject": subject,
        })
        if acr is not UNSET:
            field_dict["acr"] = acr
        if context is not UNSET:
            field_dict["context"] = context
        if force_subject_identifier is not UNSET:
            field_dict["force_subject_identifier"] = force_subject_identifier
        if remember is not UNSET:
            field_dict["remember"] = remember
        if remember_for is not UNSET:
            field_dict["remember_for"] = remember_for

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        subject = _d.pop("subject")

        acr = _d.pop("acr", UNSET)

        _context = _d.pop("context", UNSET)
        context: Union[Unset, JSONRawMessage]
        if isinstance(_context,  Unset):
            context = UNSET
        else:
            context = JSONRawMessage.from_dict(_context)




        force_subject_identifier = _d.pop("force_subject_identifier", UNSET)

        remember = _d.pop("remember", UNSET)

        remember_for = _d.pop("remember_for", UNSET)

        accept_login_request = cls(
            subject=subject,
            acr=acr,
            context=context,
            force_subject_identifier=force_subject_identifier,
            remember=remember,
            remember_for=remember_for,
        )

        accept_login_request.additional_properties = _d
        return accept_login_request

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
