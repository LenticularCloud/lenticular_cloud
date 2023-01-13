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




T = TypeVar("T", bound="OAuth2Client")

@attr.s(auto_attribs=True)
class OAuth2Client:
    """
    Attributes:
        allowed_cors_origins (Union[Unset, List[str]]):
        audience (Union[Unset, List[str]]):
        backchannel_logout_session_required (Union[Unset, bool]): Boolean value specifying whether the RP requires that
            a sid (session ID) Claim be included in the Logout
            Token to identify the RP session with the OP when the backchannel_logout_uri is used.
            If omitted, the default value is false.
        backchannel_logout_uri (Union[Unset, str]): RP URL that will cause the RP to log itself out when sent a Logout
            Token by the OP.
        client_id (Union[Unset, str]): ID  is the id for this client.
        client_name (Union[Unset, str]): Name is the human-readable string name of the client to be presented to the
            end-user during authorization.
        client_secret (Union[Unset, str]): Secret is the client's secret. The secret will be included in the create
            request as cleartext, and then
            never again. The secret is stored using BCrypt so it is impossible to recover it. Tell your users
            that they need to write the secret down as it will not be made available again.
        client_secret_expires_at (Union[Unset, int]): SecretExpiresAt is an integer holding the time at which the client
            secret will expire or 0 if it will not expire. The time is
            represented as the number of seconds from 1970-01-01T00:00:00Z as
            measured in UTC until the date/time of expiration.

            This feature is currently not supported and it's value will always
            be set to 0.
        client_uri (Union[Unset, str]): ClientURI is an URL string of a web page providing information about the client.
            If present, the server SHOULD display this URL to the end-user in
            a clickable fashion.
        contacts (Union[Unset, List[str]]):
        created_at (Union[Unset, datetime.datetime]): CreatedAt returns the timestamp of the client's creation.
        frontchannel_logout_session_required (Union[Unset, bool]): Boolean value specifying whether the RP requires that
            iss (issuer) and sid (session ID) query parameters be
            included to identify the RP session with the OP when the frontchannel_logout_uri is used.
            If omitted, the default value is false.
        frontchannel_logout_uri (Union[Unset, str]): RP URL that will cause the RP to log itself out when rendered in an
            iframe by the OP. An iss (issuer) query
            parameter and a sid (session ID) query parameter MAY be included by the OP to enable the RP to validate the
            request and to determine which of the potentially multiple sessions is to be logged out; if either is
            included, both MUST be.
        grant_types (Union[Unset, List[str]]):
        jwks (Union[Unset, JoseJSONWebKeySet]):
        jwks_uri (Union[Unset, str]): URL for the Client's JSON Web Key Set [JWK] document. If the Client signs requests
            to the Server, it contains
            the signing key(s) the Server uses to validate signatures from the Client. The JWK Set MAY also contain the
            Client's encryption keys(s), which are used by the Server to encrypt responses to the Client. When both signing
            and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the
            referenced
            JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both
            signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used
            to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST
            match those in the certificate.
        logo_uri (Union[Unset, str]): LogoURI is an URL string that references a logo for the client.
        metadata (Union[Unset, JSONRawMessage]):
        owner (Union[Unset, str]): Owner is a string identifying the owner of the OAuth 2.0 Client.
        policy_uri (Union[Unset, str]): PolicyURI is a URL string that points to a human-readable privacy policy
            document
            that describes how the deployment organization collects, uses,
            retains, and discloses personal data.
        post_logout_redirect_uris (Union[Unset, List[str]]):
        redirect_uris (Union[Unset, List[str]]):
        request_object_signing_alg (Union[Unset, str]): JWS [JWS] alg algorithm [JWA] that MUST be used for signing
            Request Objects sent to the OP. All Request Objects
            from this Client MUST be rejected, if not signed with this algorithm.
        request_uris (Union[Unset, List[str]]):
        response_types (Union[Unset, List[str]]):
        scope (Union[Unset, str]): Scope is a string containing a space-separated list of scope values (as
            described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client
            can use when requesting access tokens.
        sector_identifier_uri (Union[Unset, str]): URL using the https scheme to be used in calculating Pseudonymous
            Identifiers by the OP. The URL references a
            file with a single JSON array of redirect_uri values.
        subject_type (Union[Unset, str]): SubjectType requested for responses to this Client. The
            subject_types_supported Discovery parameter contains a
            list of the supported subject_type values for this server. Valid types include `pairwise` and `public`.
        token_endpoint_auth_method (Union[Unset, str]): Requested Client Authentication method for the Token Endpoint.
            The options are client_secret_post,
            client_secret_basic, private_key_jwt, and none.
        token_endpoint_auth_signing_alg (Union[Unset, str]): Requested Client Authentication signing algorithm for the
            Token Endpoint.
        tos_uri (Union[Unset, str]): TermsOfServiceURI is a URL string that points to a human-readable terms of service
            document for the client that describes a contractual relationship
            between the end-user and the client that the end-user accepts when
            authorizing the client.
        updated_at (Union[Unset, datetime.datetime]): UpdatedAt returns the timestamp of the last update.
        userinfo_signed_response_alg (Union[Unset, str]): JWS alg algorithm [JWA] REQUIRED for signing UserInfo
            Responses. If this is specified, the response will be JWT
            [JWT] serialized, and signed using JWS. The default, if omitted, is for the UserInfo Response to return the
            Claims
            as a UTF-8 encoded JSON object using the application/json content-type.
    """

    allowed_cors_origins: Union[Unset, List[str]] = UNSET
    audience: Union[Unset, List[str]] = UNSET
    backchannel_logout_session_required: Union[Unset, bool] = UNSET
    backchannel_logout_uri: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    client_name: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    client_secret_expires_at: Union[Unset, int] = UNSET
    client_uri: Union[Unset, str] = UNSET
    contacts: Union[Unset, List[str]] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    frontchannel_logout_session_required: Union[Unset, bool] = UNSET
    frontchannel_logout_uri: Union[Unset, str] = UNSET
    grant_types: Union[Unset, List[str]] = UNSET
    jwks: Union[Unset, 'JoseJSONWebKeySet'] = UNSET
    jwks_uri: Union[Unset, str] = UNSET
    logo_uri: Union[Unset, str] = UNSET
    metadata: Union[Unset, 'JSONRawMessage'] = UNSET
    owner: Union[Unset, str] = UNSET
    policy_uri: Union[Unset, str] = UNSET
    post_logout_redirect_uris: Union[Unset, List[str]] = UNSET
    redirect_uris: Union[Unset, List[str]] = UNSET
    request_object_signing_alg: Union[Unset, str] = UNSET
    request_uris: Union[Unset, List[str]] = UNSET
    response_types: Union[Unset, List[str]] = UNSET
    scope: Union[Unset, str] = UNSET
    sector_identifier_uri: Union[Unset, str] = UNSET
    subject_type: Union[Unset, str] = UNSET
    token_endpoint_auth_method: Union[Unset, str] = UNSET
    token_endpoint_auth_signing_alg: Union[Unset, str] = UNSET
    tos_uri: Union[Unset, str] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    userinfo_signed_response_alg: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        allowed_cors_origins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.allowed_cors_origins, Unset):
            allowed_cors_origins = self.allowed_cors_origins




        audience: Union[Unset, List[str]] = UNSET
        if not isinstance(self.audience, Unset):
            audience = self.audience




        backchannel_logout_session_required = self.backchannel_logout_session_required
        backchannel_logout_uri = self.backchannel_logout_uri
        client_id = self.client_id
        client_name = self.client_name
        client_secret = self.client_secret
        client_secret_expires_at = self.client_secret_expires_at
        client_uri = self.client_uri
        contacts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = self.contacts




        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        frontchannel_logout_session_required = self.frontchannel_logout_session_required
        frontchannel_logout_uri = self.frontchannel_logout_uri
        grant_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.grant_types, Unset):
            grant_types = self.grant_types




        jwks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwks, Unset):
            jwks = self.jwks.to_dict()

        jwks_uri = self.jwks_uri
        logo_uri = self.logo_uri
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        owner = self.owner
        policy_uri = self.policy_uri
        post_logout_redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.post_logout_redirect_uris, Unset):
            post_logout_redirect_uris = self.post_logout_redirect_uris




        redirect_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.redirect_uris, Unset):
            redirect_uris = self.redirect_uris




        request_object_signing_alg = self.request_object_signing_alg
        request_uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.request_uris, Unset):
            request_uris = self.request_uris




        response_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.response_types, Unset):
            response_types = self.response_types




        scope = self.scope
        sector_identifier_uri = self.sector_identifier_uri
        subject_type = self.subject_type
        token_endpoint_auth_method = self.token_endpoint_auth_method
        token_endpoint_auth_signing_alg = self.token_endpoint_auth_signing_alg
        tos_uri = self.tos_uri
        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        userinfo_signed_response_alg = self.userinfo_signed_response_alg

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allowed_cors_origins is not UNSET:
            field_dict["allowed_cors_origins"] = allowed_cors_origins
        if audience is not UNSET:
            field_dict["audience"] = audience
        if backchannel_logout_session_required is not UNSET:
            field_dict["backchannel_logout_session_required"] = backchannel_logout_session_required
        if backchannel_logout_uri is not UNSET:
            field_dict["backchannel_logout_uri"] = backchannel_logout_uri
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if client_secret_expires_at is not UNSET:
            field_dict["client_secret_expires_at"] = client_secret_expires_at
        if client_uri is not UNSET:
            field_dict["client_uri"] = client_uri
        if contacts is not UNSET:
            field_dict["contacts"] = contacts
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if frontchannel_logout_session_required is not UNSET:
            field_dict["frontchannel_logout_session_required"] = frontchannel_logout_session_required
        if frontchannel_logout_uri is not UNSET:
            field_dict["frontchannel_logout_uri"] = frontchannel_logout_uri
        if grant_types is not UNSET:
            field_dict["grant_types"] = grant_types
        if jwks is not UNSET:
            field_dict["jwks"] = jwks
        if jwks_uri is not UNSET:
            field_dict["jwks_uri"] = jwks_uri
        if logo_uri is not UNSET:
            field_dict["logo_uri"] = logo_uri
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if owner is not UNSET:
            field_dict["owner"] = owner
        if policy_uri is not UNSET:
            field_dict["policy_uri"] = policy_uri
        if post_logout_redirect_uris is not UNSET:
            field_dict["post_logout_redirect_uris"] = post_logout_redirect_uris
        if redirect_uris is not UNSET:
            field_dict["redirect_uris"] = redirect_uris
        if request_object_signing_alg is not UNSET:
            field_dict["request_object_signing_alg"] = request_object_signing_alg
        if request_uris is not UNSET:
            field_dict["request_uris"] = request_uris
        if response_types is not UNSET:
            field_dict["response_types"] = response_types
        if scope is not UNSET:
            field_dict["scope"] = scope
        if sector_identifier_uri is not UNSET:
            field_dict["sector_identifier_uri"] = sector_identifier_uri
        if subject_type is not UNSET:
            field_dict["subject_type"] = subject_type
        if token_endpoint_auth_method is not UNSET:
            field_dict["token_endpoint_auth_method"] = token_endpoint_auth_method
        if token_endpoint_auth_signing_alg is not UNSET:
            field_dict["token_endpoint_auth_signing_alg"] = token_endpoint_auth_signing_alg
        if tos_uri is not UNSET:
            field_dict["tos_uri"] = tos_uri
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if userinfo_signed_response_alg is not UNSET:
            field_dict["userinfo_signed_response_alg"] = userinfo_signed_response_alg

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        allowed_cors_origins = cast(List[str], _d.pop("allowed_cors_origins", UNSET))


        audience = cast(List[str], _d.pop("audience", UNSET))


        backchannel_logout_session_required = _d.pop("backchannel_logout_session_required", UNSET)

        backchannel_logout_uri = _d.pop("backchannel_logout_uri", UNSET)

        client_id = _d.pop("client_id", UNSET)

        client_name = _d.pop("client_name", UNSET)

        client_secret = _d.pop("client_secret", UNSET)

        client_secret_expires_at = _d.pop("client_secret_expires_at", UNSET)

        client_uri = _d.pop("client_uri", UNSET)

        contacts = cast(List[str], _d.pop("contacts", UNSET))


        _created_at = _d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        frontchannel_logout_session_required = _d.pop("frontchannel_logout_session_required", UNSET)

        frontchannel_logout_uri = _d.pop("frontchannel_logout_uri", UNSET)

        grant_types = cast(List[str], _d.pop("grant_types", UNSET))


        _jwks = _d.pop("jwks", UNSET)
        jwks: Union[Unset, JoseJSONWebKeySet]
        if isinstance(_jwks,  Unset):
            jwks = UNSET
        else:
            jwks = JoseJSONWebKeySet.from_dict(_jwks)




        jwks_uri = _d.pop("jwks_uri", UNSET)

        logo_uri = _d.pop("logo_uri", UNSET)

        _metadata = _d.pop("metadata", UNSET)
        metadata: Union[Unset, JSONRawMessage]
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = JSONRawMessage.from_dict(_metadata)




        owner = _d.pop("owner", UNSET)

        policy_uri = _d.pop("policy_uri", UNSET)

        post_logout_redirect_uris = cast(List[str], _d.pop("post_logout_redirect_uris", UNSET))


        redirect_uris = cast(List[str], _d.pop("redirect_uris", UNSET))


        request_object_signing_alg = _d.pop("request_object_signing_alg", UNSET)

        request_uris = cast(List[str], _d.pop("request_uris", UNSET))


        response_types = cast(List[str], _d.pop("response_types", UNSET))


        scope = _d.pop("scope", UNSET)

        sector_identifier_uri = _d.pop("sector_identifier_uri", UNSET)

        subject_type = _d.pop("subject_type", UNSET)

        token_endpoint_auth_method = _d.pop("token_endpoint_auth_method", UNSET)

        token_endpoint_auth_signing_alg = _d.pop("token_endpoint_auth_signing_alg", UNSET)

        tos_uri = _d.pop("tos_uri", UNSET)

        _updated_at = _d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        userinfo_signed_response_alg = _d.pop("userinfo_signed_response_alg", UNSET)

        o_auth_2_client = cls(
            allowed_cors_origins=allowed_cors_origins,
            audience=audience,
            backchannel_logout_session_required=backchannel_logout_session_required,
            backchannel_logout_uri=backchannel_logout_uri,
            client_id=client_id,
            client_name=client_name,
            client_secret=client_secret,
            client_secret_expires_at=client_secret_expires_at,
            client_uri=client_uri,
            contacts=contacts,
            created_at=created_at,
            frontchannel_logout_session_required=frontchannel_logout_session_required,
            frontchannel_logout_uri=frontchannel_logout_uri,
            grant_types=grant_types,
            jwks=jwks,
            jwks_uri=jwks_uri,
            logo_uri=logo_uri,
            metadata=metadata,
            owner=owner,
            policy_uri=policy_uri,
            post_logout_redirect_uris=post_logout_redirect_uris,
            redirect_uris=redirect_uris,
            request_object_signing_alg=request_object_signing_alg,
            request_uris=request_uris,
            response_types=response_types,
            scope=scope,
            sector_identifier_uri=sector_identifier_uri,
            subject_type=subject_type,
            token_endpoint_auth_method=token_endpoint_auth_method,
            token_endpoint_auth_signing_alg=token_endpoint_auth_signing_alg,
            tos_uri=tos_uri,
            updated_at=updated_at,
            userinfo_signed_response_alg=userinfo_signed_response_alg,
        )

        o_auth_2_client.additional_properties = _d
        return o_auth_2_client

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
