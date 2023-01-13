from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from typing import Dict
from typing import cast, List

if TYPE_CHECKING:
  from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
  from ..models.o_auth_20_client import OAuth20Client




T = TypeVar("T", bound="ContainsInformationOnAnOngoingConsentRequest")

@attr.s(auto_attribs=True)
class ContainsInformationOnAnOngoingConsentRequest:
    """
    Attributes:
        challenge (str): ID is the identifier ("authorization challenge") of the consent authorization request. It is
            used to
            identify the session.
        acr (Union[Unset, str]): ACR represents the Authentication AuthorizationContext Class Reference value for this
            authentication session. You can use it
            to express that, for example, a user authenticated using two factor authentication.
        amr (Union[Unset, List[str]]):
        client (Union[Unset, OAuth20Client]): OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID Connect flows.
            Usually, OAuth 2.0 clients are
            generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.
        context (Union[Unset, Any]):
        login_challenge (Union[Unset, str]): LoginChallenge is the login challenge this consent challenge belongs to. It
            can be used to associate
            a login and consent request in the login & consent app.
        login_session_id (Union[Unset, str]): LoginSessionID is the login session ID. If the user-agent reuses a login
            session (via cookie / remember flag)
            this ID will remain the same. If the user-agent did not have an existing authentication session (e.g. remember
            is false)
            this will be a new random value. This value is used as the "sid" parameter in the ID Token and in OIDC
            Front-/Back-
            channel logout. It's value can generally be used to associate consecutive login requests by a certain user.
        oidc_context (Union[Unset, ContainsOptionalInformationAboutTheOpenIDConnectRequest]):
        request_url (Union[Unset, str]): RequestURL is the original OAuth 2.0 Authorization URL requested by the OAuth
            2.0 client. It is the URL which
            initiates the OAuth 2.0 Authorization Code or OAuth 2.0 Implicit flow. This URL is typically not needed, but
            might come in handy if you want to deal with additional request parameters.
        requested_access_token_audience (Union[Unset, List[str]]):
        requested_scope (Union[Unset, List[str]]):
        skip (Union[Unset, bool]): Skip, if true, implies that the client has requested the same scopes from the same
            user previously.
            If true, you must not ask the user to grant the requested scopes. You must however either allow or deny the
            consent request using the usual API call.
        subject (Union[Unset, str]): Subject is the user ID of the end-user that authenticated. Now, that end user needs
            to grant or deny the scope
            requested by the OAuth 2.0 client.
    """

    challenge: str
    acr: Union[Unset, str] = UNSET
    amr: Union[Unset, List[str]] = UNSET
    client: Union[Unset, 'OAuth20Client'] = UNSET
    context: Union[Unset, Any] = UNSET
    login_challenge: Union[Unset, str] = UNSET
    login_session_id: Union[Unset, str] = UNSET
    oidc_context: Union[Unset, 'ContainsOptionalInformationAboutTheOpenIDConnectRequest'] = UNSET
    request_url: Union[Unset, str] = UNSET
    requested_access_token_audience: Union[Unset, List[str]] = UNSET
    requested_scope: Union[Unset, List[str]] = UNSET
    skip: Union[Unset, bool] = UNSET
    subject: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
        from ..models.o_auth_20_client import OAuth20Client
        challenge = self.challenge
        acr = self.acr
        amr: Union[Unset, List[str]] = UNSET
        if not isinstance(self.amr, Unset):
            amr = self.amr




        client: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.client, Unset):
            client = self.client.to_dict()

        context = self.context
        login_challenge = self.login_challenge
        login_session_id = self.login_session_id
        oidc_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.oidc_context, Unset):
            oidc_context = self.oidc_context.to_dict()

        request_url = self.request_url
        requested_access_token_audience: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requested_access_token_audience, Unset):
            requested_access_token_audience = self.requested_access_token_audience




        requested_scope: Union[Unset, List[str]] = UNSET
        if not isinstance(self.requested_scope, Unset):
            requested_scope = self.requested_scope




        skip = self.skip
        subject = self.subject

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "challenge": challenge,
        })
        if acr is not UNSET:
            field_dict["acr"] = acr
        if amr is not UNSET:
            field_dict["amr"] = amr
        if client is not UNSET:
            field_dict["client"] = client
        if context is not UNSET:
            field_dict["context"] = context
        if login_challenge is not UNSET:
            field_dict["login_challenge"] = login_challenge
        if login_session_id is not UNSET:
            field_dict["login_session_id"] = login_session_id
        if oidc_context is not UNSET:
            field_dict["oidc_context"] = oidc_context
        if request_url is not UNSET:
            field_dict["request_url"] = request_url
        if requested_access_token_audience is not UNSET:
            field_dict["requested_access_token_audience"] = requested_access_token_audience
        if requested_scope is not UNSET:
            field_dict["requested_scope"] = requested_scope
        if skip is not UNSET:
            field_dict["skip"] = skip
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.contains_optional_information_about_the_open_id_connect_request import ContainsOptionalInformationAboutTheOpenIDConnectRequest
        from ..models.o_auth_20_client import OAuth20Client
        _d = src_dict.copy()
        challenge = _d.pop("challenge")

        acr = _d.pop("acr", UNSET)

        amr = cast(List[str], _d.pop("amr", UNSET))


        _client = _d.pop("client", UNSET)
        client: Union[Unset, OAuth20Client]
        if isinstance(_client,  Unset):
            client = UNSET
        else:
            client = OAuth20Client.from_dict(_client)




        context = _d.pop("context", UNSET)

        login_challenge = _d.pop("login_challenge", UNSET)

        login_session_id = _d.pop("login_session_id", UNSET)

        _oidc_context = _d.pop("oidc_context", UNSET)
        oidc_context: Union[Unset, ContainsOptionalInformationAboutTheOpenIDConnectRequest]
        if isinstance(_oidc_context,  Unset):
            oidc_context = UNSET
        else:
            oidc_context = ContainsOptionalInformationAboutTheOpenIDConnectRequest.from_dict(_oidc_context)




        request_url = _d.pop("request_url", UNSET)

        requested_access_token_audience = cast(List[str], _d.pop("requested_access_token_audience", UNSET))


        requested_scope = cast(List[str], _d.pop("requested_scope", UNSET))


        skip = _d.pop("skip", UNSET)

        subject = _d.pop("subject", UNSET)

        contains_information_on_an_ongoing_consent_request = cls(
            challenge=challenge,
            acr=acr,
            amr=amr,
            client=client,
            context=context,
            login_challenge=login_challenge,
            login_session_id=login_session_id,
            oidc_context=oidc_context,
            request_url=request_url,
            requested_access_token_audience=requested_access_token_audience,
            requested_scope=requested_scope,
            skip=skip,
            subject=subject,
        )

        contains_information_on_an_ongoing_consent_request.additional_properties = _d
        return contains_information_on_an_ongoing_consent_request

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
