from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import Dict
from typing import cast, List

if TYPE_CHECKING:
  from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
  from ..models.o_auth_20_client import OAuth20Client




T = TypeVar("T", bound="ContainsInformationOnAnOngoingLoginRequest")

@attr.s(auto_attribs=True)
class ContainsInformationOnAnOngoingLoginRequest:
    """
    Attributes:
        challenge (str): ID is the identifier ("login challenge") of the login request. It is used to
            identify the session.
        client (OAuth20Client): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth
            2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
        request_url (str): RequestURL is the original OAuth 2.0 Authorization URL requested by the OAuth 2.0 client. It
            is the URL which
            initiates the OAuth 2.0 Authorization Code or OAuth 2.0 Implicit flow. This URL is typically not needed, but
            might come in handy if you want to deal with additional request parameters.
        requested_access_token_audience (List[str]):
        requested_scope (List[str]):
        skip (bool): Skip, if true, implies that the client has requested the same scopes from the same user previously.
            If true, you can skip asking the user to grant the requested scopes, and simply forward the user to the redirect
            URL.

            This feature allows you to update / set session information.
        subject (str): Subject is the user ID of the end-user that authenticated. Now, that end user needs to grant or
            deny the scope
            requested by the OAuth 2.0 client. If this value is set and `skip` is true, you MUST include this subject type
            when accepting the login request, or the request will fail.
        oidc_context (Union[Unset, ContainsOptionalInformationAboutTheOpenIDConnectRequest]):
        session_id (Union[Unset, str]): SessionID is the login session ID. If the user-agent reuses a login session (via
            cookie / remember flag)
            this ID will remain the same. If the user-agent did not have an existing authentication session (e.g. remember
            is false)
            this will be a new random value. This value is used as the "sid" parameter in the ID Token and in OIDC
            Front-/Back-
            channel logout. It's value can generally be used to associate consecutive login requests by a certain user.
    """

    challenge: str
    client: 'OAuth20Client'
    request_url: str
    requested_access_token_audience: List[str]
    requested_scope: List[str]
    skip: bool
    subject: str
    oidc_context: Union[Unset, 'ContainsOptionalInformationAboutTheOpenIDConnectRequest'] = UNSET
    session_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
        from ..models.o_auth_20_client import OAuth20Client
        challenge = self.challenge
        client = self.client.to_dict()

        request_url = self.request_url
        requested_access_token_audience = self.requested_access_token_audience




        requested_scope = self.requested_scope




        skip = self.skip
        subject = self.subject
        oidc_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oidc_context, Unset):
            oidc_context = self.oidc_context.to_dict()

        session_id = self.session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "challenge": challenge,
            "client": client,
            "request_url": request_url,
            "requested_access_token_audience": requested_access_token_audience,
            "requested_scope": requested_scope,
            "skip": skip,
            "subject": subject,
        })
        if oidc_context is not UNSET:
            field_dict["oidc_context"] = oidc_context
        if session_id is not UNSET:
            field_dict["session_id"] = session_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
        from ..models.o_auth_20_client import OAuth20Client
        _d = src_dict.copy()
        challenge = _d.pop("challenge")

        client = OAuth20Client.from_dict(_d.pop("client"))




        request_url = _d.pop("request_url")

        requested_access_token_audience = cast(List[str], _d.pop("requested_access_token_audience"))


        requested_scope = cast(List[str], _d.pop("requested_scope"))


        skip = _d.pop("skip")

        subject = _d.pop("subject")

        _oidc_context = _d.pop("oidc_context", UNSET)
        oidc_context: Union[Unset, ContainsOptionalInformationAboutTheOpenIDConnectRequest]
        if isinstance(_oidc_context,  Unset):
            oidc_context = UNSET
        else:
            oidc_context = ContainsOptionalInformationAboutTheOpenIDConnectRequest.from_dict(_oidc_context)




        session_id = _d.pop("session_id", UNSET)

        contains_information_on_an_ongoing_login_request = cls(
            challenge=challenge,
            client=client,
            request_url=request_url,
            requested_access_token_audience=requested_access_token_audience,
            requested_scope=requested_scope,
            skip=skip,
            subject=subject,
            oidc_context=oidc_context,
            session_id=session_id,
        )

        contains_information_on_an_ongoing_login_request.additional_properties = _d
        return contains_information_on_an_ongoing_login_request

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
