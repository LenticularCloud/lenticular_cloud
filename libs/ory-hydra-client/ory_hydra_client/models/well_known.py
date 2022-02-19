from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WellKnown")


@attr.s(auto_attribs=True)
class WellKnown:
    """It includes links to several endpoints (e.g. /oauth2/token) and exposes information on supported signature
    algorithms
    among others.

        Attributes:
            authorization_endpoint (str): URL of the OP's OAuth 2.0 Authorization Endpoint. Example:
                https://playground.ory.sh/ory-hydra/public/oauth2/auth.
            id_token_signing_alg_values_supported (List[str]): JSON array containing a list of the JWS signing algorithms
                (alg values) supported by the OP for the ID Token
                to encode the Claims in a JWT.
            issuer (str): URL using the https scheme with no query or fragment component that the OP asserts as its
                IssuerURL Identifier.
                If IssuerURL discovery is supported , this value MUST be identical to the issuer value returned
                by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this IssuerURL.
                Example: https://playground.ory.sh/ory-hydra/public/.
            jwks_uri (str): URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to
                validate
                signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs
                to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use)
                parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage.
                Although some algorithms allow the same key to be used for both signatures and encryption, doing so is
                NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of
                keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.
                Example: https://playground.ory.sh/ory-hydra/public/.well-known/jwks.json.
            response_types_supported (List[str]): JSON array containing a list of the OAuth 2.0 response_type values that
                this OP supports. Dynamic OpenID
                Providers MUST support the code, id_token, and the token id_token Response Type values.
            subject_types_supported (List[str]): JSON array containing a list of the Subject Identifier types that this OP
                supports. Valid types include
                pairwise and public.
            token_endpoint (str): URL of the OP's OAuth 2.0 Token Endpoint Example: https://playground.ory.sh/ory-
                hydra/public/oauth2/token.
            backchannel_logout_session_supported (Union[Unset, bool]): Boolean value specifying whether the OP can pass a
                sid (session ID) Claim in the Logout Token to identify the RP
                session with the OP. If supported, the sid Claim is also included in ID Tokens issued by the OP
            backchannel_logout_supported (Union[Unset, bool]): Boolean value specifying whether the OP supports back-channel
                logout, with true indicating support.
            claims_parameter_supported (Union[Unset, bool]): Boolean value specifying whether the OP supports use of the
                claims parameter, with true indicating support.
            claims_supported (Union[Unset, List[str]]): JSON array containing a list of the Claim Names of the Claims that
                the OpenID Provider MAY be able to supply
                values for. Note that for privacy or other reasons, this might not be an exhaustive list.
            end_session_endpoint (Union[Unset, str]): URL at the OP to which an RP can perform a redirect to request that
                the End-User be logged out at the OP.
            frontchannel_logout_session_supported (Union[Unset, bool]): Boolean value specifying whether the OP can pass iss
                (issuer) and sid (session ID) query parameters to identify
                the RP session with the OP when the frontchannel_logout_uri is used. If supported, the sid Claim is also
                included in ID Tokens issued by the OP.
            frontchannel_logout_supported (Union[Unset, bool]): Boolean value specifying whether the OP supports HTTP-based
                logout, with true indicating support.
            grant_types_supported (Union[Unset, List[str]]): JSON array containing a list of the OAuth 2.0 Grant Type values
                that this OP supports.
            registration_endpoint (Union[Unset, str]): URL of the OP's Dynamic Client Registration Endpoint. Example:
                https://playground.ory.sh/ory-hydra/admin/client.
            request_object_signing_alg_values_supported (Union[Unset, List[str]]): JSON array containing a list of the JWS
                signing algorithms (alg values) supported by the OP for Request Objects,
                which are described in Section 6.1 of OpenID Connect Core 1.0 [OpenID.Core]. These algorithms are used both when
                the Request Object is passed by value (using the request parameter) and when it is passed by reference
                (using the request_uri parameter).
            request_parameter_supported (Union[Unset, bool]): Boolean value specifying whether the OP supports use of the
                request parameter, with true indicating support.
            request_uri_parameter_supported (Union[Unset, bool]): Boolean value specifying whether the OP supports use of
                the request_uri parameter, with true indicating support.
            require_request_uri_registration (Union[Unset, bool]): Boolean value specifying whether the OP requires any
                request_uri values used to be pre-registered
                using the request_uris registration parameter.
            response_modes_supported (Union[Unset, List[str]]): JSON array containing a list of the OAuth 2.0 response_mode
                values that this OP supports.
            revocation_endpoint (Union[Unset, str]): URL of the authorization server's OAuth 2.0 revocation endpoint.
            scopes_supported (Union[Unset, List[str]]): SON array containing a list of the OAuth 2.0 [RFC6749] scope values
                that this server supports. The server MUST
                support the openid scope value. Servers MAY choose not to advertise some supported scope values even when this
                parameter is used
            token_endpoint_auth_methods_supported (Union[Unset, List[str]]): JSON array containing a list of Client
                Authentication methods supported by this Token Endpoint. The options are
                client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of
                OpenID Connect Core 1.0
            userinfo_endpoint (Union[Unset, str]): URL of the OP's UserInfo Endpoint.
            userinfo_signing_alg_values_supported (Union[Unset, List[str]]): JSON array containing a list of the JWS [JWS]
                signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT [JWT].
    """

    authorization_endpoint: str
    id_token_signing_alg_values_supported: List[str]
    issuer: str
    jwks_uri: str
    response_types_supported: List[str]
    subject_types_supported: List[str]
    token_endpoint: str
    backchannel_logout_session_supported: Union[Unset, bool] = UNSET
    backchannel_logout_supported: Union[Unset, bool] = UNSET
    claims_parameter_supported: Union[Unset, bool] = UNSET
    claims_supported: Union[Unset, List[str]] = UNSET
    end_session_endpoint: Union[Unset, str] = UNSET
    frontchannel_logout_session_supported: Union[Unset, bool] = UNSET
    frontchannel_logout_supported: Union[Unset, bool] = UNSET
    grant_types_supported: Union[Unset, List[str]] = UNSET
    registration_endpoint: Union[Unset, str] = UNSET
    request_object_signing_alg_values_supported: Union[Unset, List[str]] = UNSET
    request_parameter_supported: Union[Unset, bool] = UNSET
    request_uri_parameter_supported: Union[Unset, bool] = UNSET
    require_request_uri_registration: Union[Unset, bool] = UNSET
    response_modes_supported: Union[Unset, List[str]] = UNSET
    revocation_endpoint: Union[Unset, str] = UNSET
    scopes_supported: Union[Unset, List[str]] = UNSET
    token_endpoint_auth_methods_supported: Union[Unset, List[str]] = UNSET
    userinfo_endpoint: Union[Unset, str] = UNSET
    userinfo_signing_alg_values_supported: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authorization_endpoint = self.authorization_endpoint
        id_token_signing_alg_values_supported = self.id_token_signing_alg_values_supported

        issuer = self.issuer
        jwks_uri = self.jwks_uri
        response_types_supported = self.response_types_supported

        subject_types_supported = self.subject_types_supported

        token_endpoint = self.token_endpoint
        backchannel_logout_session_supported = self.backchannel_logout_session_supported
        backchannel_logout_supported = self.backchannel_logout_supported
        claims_parameter_supported = self.claims_parameter_supported
        claims_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.claims_supported, Unset):
            claims_supported = self.claims_supported

        end_session_endpoint = self.end_session_endpoint
        frontchannel_logout_session_supported = self.frontchannel_logout_session_supported
        frontchannel_logout_supported = self.frontchannel_logout_supported
        grant_types_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.grant_types_supported, Unset):
            grant_types_supported = self.grant_types_supported

        registration_endpoint = self.registration_endpoint
        request_object_signing_alg_values_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.request_object_signing_alg_values_supported, Unset):
            request_object_signing_alg_values_supported = self.request_object_signing_alg_values_supported

        request_parameter_supported = self.request_parameter_supported
        request_uri_parameter_supported = self.request_uri_parameter_supported
        require_request_uri_registration = self.require_request_uri_registration
        response_modes_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.response_modes_supported, Unset):
            response_modes_supported = self.response_modes_supported

        revocation_endpoint = self.revocation_endpoint
        scopes_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.scopes_supported, Unset):
            scopes_supported = self.scopes_supported

        token_endpoint_auth_methods_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.token_endpoint_auth_methods_supported, Unset):
            token_endpoint_auth_methods_supported = self.token_endpoint_auth_methods_supported

        userinfo_endpoint = self.userinfo_endpoint
        userinfo_signing_alg_values_supported: Union[Unset, List[str]] = UNSET
        if not isinstance(self.userinfo_signing_alg_values_supported, Unset):
            userinfo_signing_alg_values_supported = self.userinfo_signing_alg_values_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorization_endpoint": authorization_endpoint,
                "id_token_signing_alg_values_supported": id_token_signing_alg_values_supported,
                "issuer": issuer,
                "jwks_uri": jwks_uri,
                "response_types_supported": response_types_supported,
                "subject_types_supported": subject_types_supported,
                "token_endpoint": token_endpoint,
            }
        )
        if backchannel_logout_session_supported is not UNSET:
            field_dict["backchannel_logout_session_supported"] = backchannel_logout_session_supported
        if backchannel_logout_supported is not UNSET:
            field_dict["backchannel_logout_supported"] = backchannel_logout_supported
        if claims_parameter_supported is not UNSET:
            field_dict["claims_parameter_supported"] = claims_parameter_supported
        if claims_supported is not UNSET:
            field_dict["claims_supported"] = claims_supported
        if end_session_endpoint is not UNSET:
            field_dict["end_session_endpoint"] = end_session_endpoint
        if frontchannel_logout_session_supported is not UNSET:
            field_dict["frontchannel_logout_session_supported"] = frontchannel_logout_session_supported
        if frontchannel_logout_supported is not UNSET:
            field_dict["frontchannel_logout_supported"] = frontchannel_logout_supported
        if grant_types_supported is not UNSET:
            field_dict["grant_types_supported"] = grant_types_supported
        if registration_endpoint is not UNSET:
            field_dict["registration_endpoint"] = registration_endpoint
        if request_object_signing_alg_values_supported is not UNSET:
            field_dict["request_object_signing_alg_values_supported"] = request_object_signing_alg_values_supported
        if request_parameter_supported is not UNSET:
            field_dict["request_parameter_supported"] = request_parameter_supported
        if request_uri_parameter_supported is not UNSET:
            field_dict["request_uri_parameter_supported"] = request_uri_parameter_supported
        if require_request_uri_registration is not UNSET:
            field_dict["require_request_uri_registration"] = require_request_uri_registration
        if response_modes_supported is not UNSET:
            field_dict["response_modes_supported"] = response_modes_supported
        if revocation_endpoint is not UNSET:
            field_dict["revocation_endpoint"] = revocation_endpoint
        if scopes_supported is not UNSET:
            field_dict["scopes_supported"] = scopes_supported
        if token_endpoint_auth_methods_supported is not UNSET:
            field_dict["token_endpoint_auth_methods_supported"] = token_endpoint_auth_methods_supported
        if userinfo_endpoint is not UNSET:
            field_dict["userinfo_endpoint"] = userinfo_endpoint
        if userinfo_signing_alg_values_supported is not UNSET:
            field_dict["userinfo_signing_alg_values_supported"] = userinfo_signing_alg_values_supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        authorization_endpoint = _d.pop("authorization_endpoint")

        id_token_signing_alg_values_supported = cast(List[str], _d.pop("id_token_signing_alg_values_supported"))

        issuer = _d.pop("issuer")

        jwks_uri = _d.pop("jwks_uri")

        response_types_supported = cast(List[str], _d.pop("response_types_supported"))

        subject_types_supported = cast(List[str], _d.pop("subject_types_supported"))

        token_endpoint = _d.pop("token_endpoint")

        backchannel_logout_session_supported = _d.pop("backchannel_logout_session_supported", UNSET)

        backchannel_logout_supported = _d.pop("backchannel_logout_supported", UNSET)

        claims_parameter_supported = _d.pop("claims_parameter_supported", UNSET)

        claims_supported = cast(List[str], _d.pop("claims_supported", UNSET))

        end_session_endpoint = _d.pop("end_session_endpoint", UNSET)

        frontchannel_logout_session_supported = _d.pop("frontchannel_logout_session_supported", UNSET)

        frontchannel_logout_supported = _d.pop("frontchannel_logout_supported", UNSET)

        grant_types_supported = cast(List[str], _d.pop("grant_types_supported", UNSET))

        registration_endpoint = _d.pop("registration_endpoint", UNSET)

        request_object_signing_alg_values_supported = cast(
            List[str], _d.pop("request_object_signing_alg_values_supported", UNSET)
        )

        request_parameter_supported = _d.pop("request_parameter_supported", UNSET)

        request_uri_parameter_supported = _d.pop("request_uri_parameter_supported", UNSET)

        require_request_uri_registration = _d.pop("require_request_uri_registration", UNSET)

        response_modes_supported = cast(List[str], _d.pop("response_modes_supported", UNSET))

        revocation_endpoint = _d.pop("revocation_endpoint", UNSET)

        scopes_supported = cast(List[str], _d.pop("scopes_supported", UNSET))

        token_endpoint_auth_methods_supported = cast(List[str], _d.pop("token_endpoint_auth_methods_supported", UNSET))

        userinfo_endpoint = _d.pop("userinfo_endpoint", UNSET)

        userinfo_signing_alg_values_supported = cast(List[str], _d.pop("userinfo_signing_alg_values_supported", UNSET))

        well_known = cls(
            authorization_endpoint=authorization_endpoint,
            id_token_signing_alg_values_supported=id_token_signing_alg_values_supported,
            issuer=issuer,
            jwks_uri=jwks_uri,
            response_types_supported=response_types_supported,
            subject_types_supported=subject_types_supported,
            token_endpoint=token_endpoint,
            backchannel_logout_session_supported=backchannel_logout_session_supported,
            backchannel_logout_supported=backchannel_logout_supported,
            claims_parameter_supported=claims_parameter_supported,
            claims_supported=claims_supported,
            end_session_endpoint=end_session_endpoint,
            frontchannel_logout_session_supported=frontchannel_logout_session_supported,
            frontchannel_logout_supported=frontchannel_logout_supported,
            grant_types_supported=grant_types_supported,
            registration_endpoint=registration_endpoint,
            request_object_signing_alg_values_supported=request_object_signing_alg_values_supported,
            request_parameter_supported=request_parameter_supported,
            request_uri_parameter_supported=request_uri_parameter_supported,
            require_request_uri_registration=require_request_uri_registration,
            response_modes_supported=response_modes_supported,
            revocation_endpoint=revocation_endpoint,
            scopes_supported=scopes_supported,
            token_endpoint_auth_methods_supported=token_endpoint_auth_methods_supported,
            userinfo_endpoint=userinfo_endpoint,
            userinfo_signing_alg_values_supported=userinfo_signing_alg_values_supported,
        )

        well_known.additional_properties = _d
        return well_known

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
