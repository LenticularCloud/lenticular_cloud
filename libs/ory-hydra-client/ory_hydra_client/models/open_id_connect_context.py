from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import Union
from typing import Dict
from typing import cast
from ..types import UNSET, Unset
from typing import cast, List




T = TypeVar("T", bound="OpenIDConnectContext")

@attr.s(auto_attribs=True)
class OpenIDConnectContext:
    """
    Attributes:
        acr_values (Union[Unset, List[str]]): ACRValues is the Authentication AuthorizationContext Class Reference
            requested in the OAuth 2.0 Authorization request.
            It is a parameter defined by OpenID Connect and expresses which level of authentication (e.g. 2FA) is required.

            OpenID Connect defines it as follows:
            > Requested Authentication AuthorizationContext Class Reference values. Space-separated string that specifies
            the acr values
            that the Authorization Server is being requested to use for processing this Authentication Request, with the
            values appearing in order of preference. The Authentication AuthorizationContext Class satisfied by the
            authentication
            performed is returned as the acr Claim Value, as specified in Section 2. The acr Claim is requested as a
            Voluntary Claim by this parameter.
        display (Union[Unset, str]): Display is a string value that specifies how the Authorization Server displays the
            authentication and consent user interface pages to the End-User.
            The defined values are:
            page: The Authorization Server SHOULD display the authentication and consent UI consistent with a full User
            Agent page view. If the display parameter is not specified, this is the default display mode.
            popup: The Authorization Server SHOULD display the authentication and consent UI consistent with a popup User
            Agent window. The popup User Agent window should be of an appropriate size for a login-focused dialog and should
            not obscure the entire window that it is popping up over.
            touch: The Authorization Server SHOULD display the authentication and consent UI consistent with a device that
            leverages a touch interface.
            wap: The Authorization Server SHOULD display the authentication and consent UI consistent with a "feature phone"
            type display.

            The Authorization Server MAY also attempt to detect the capabilities of the User Agent and present an
            appropriate display.
        id_token_hint_claims (Union[Unset, OpenIDConnectContextIdTokenHintClaims]): IDTokenHintClaims are the claims of
            the ID Token previously issued by the Authorization Server being passed as a hint about the
            End-User's current or past authenticated session with the Client.
        login_hint (Union[Unset, str]): LoginHint hints about the login identifier the End-User might use to log in (if
            necessary).
            This hint can be used by an RP if it first asks the End-User for their e-mail address (or other identifier)
            and then wants to pass that value as a hint to the discovered authorization service. This value MAY also be a
            phone number in the format specified for the phone_number Claim. The use of this parameter is optional.
        ui_locales (Union[Unset, List[str]]): UILocales is the End-User'id preferred languages and scripts for the user
            interface, represented as a
            space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value
            "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region
            designation),
            followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested
            locales are not supported by the OpenID Provider.
    """

    acr_values: Union[Unset, List[str]] = UNSET
    display: Union[Unset, str] = UNSET
    id_token_hint_claims: Union[Unset, 'OpenIDConnectContextIdTokenHintClaims'] = UNSET
    login_hint: Union[Unset, str] = UNSET
    ui_locales: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        acr_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.acr_values, Unset):
            acr_values = self.acr_values




        display = self.display
        id_token_hint_claims: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.id_token_hint_claims, Unset):
            id_token_hint_claims = self.id_token_hint_claims.to_dict()

        login_hint = self.login_hint
        ui_locales: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ui_locales, Unset):
            ui_locales = self.ui_locales





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if acr_values is not UNSET:
            field_dict["acr_values"] = acr_values
        if display is not UNSET:
            field_dict["display"] = display
        if id_token_hint_claims is not UNSET:
            field_dict["id_token_hint_claims"] = id_token_hint_claims
        if login_hint is not UNSET:
            field_dict["login_hint"] = login_hint
        if ui_locales is not UNSET:
            field_dict["ui_locales"] = ui_locales

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        acr_values = cast(List[str], _d.pop("acr_values", UNSET))


        display = _d.pop("display", UNSET)

        _id_token_hint_claims = _d.pop("id_token_hint_claims", UNSET)
        id_token_hint_claims: Union[Unset, OpenIDConnectContextIdTokenHintClaims]
        if isinstance(_id_token_hint_claims,  Unset):
            id_token_hint_claims = UNSET
        else:
            id_token_hint_claims = OpenIDConnectContextIdTokenHintClaims.from_dict(_id_token_hint_claims)




        login_hint = _d.pop("login_hint", UNSET)

        ui_locales = cast(List[str], _d.pop("ui_locales", UNSET))


        open_id_connect_context = cls(
            acr_values=acr_values,
            display=display,
            id_token_hint_claims=id_token_hint_claims,
            login_hint=login_hint,
            ui_locales=ui_locales,
        )

        open_id_connect_context.additional_properties = _d
        return open_id_connect_context

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
