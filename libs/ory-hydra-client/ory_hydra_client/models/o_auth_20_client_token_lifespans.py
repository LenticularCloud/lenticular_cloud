from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="OAuth20ClientTokenLifespans")

@attr.s(auto_attribs=True)
class OAuth20ClientTokenLifespans:
    """Lifespans of different token types issued for this OAuth 2.0 Client.

    Attributes:
        authorization_code_grant_access_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds,
            seconds, minutes, hours.
        authorization_code_grant_id_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds,
            seconds, minutes, hours.
        authorization_code_grant_refresh_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds,
            seconds, minutes, hours.
        client_credentials_grant_access_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds,
            seconds, minutes, hours.
        implicit_grant_access_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds, seconds,
            minutes, hours.
        implicit_grant_id_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds, seconds, minutes,
            hours.
        jwt_bearer_grant_access_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds, seconds,
            minutes, hours.
        refresh_token_grant_access_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds, seconds,
            minutes, hours.
        refresh_token_grant_id_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds, seconds,
            minutes, hours.
        refresh_token_grant_refresh_token_lifespan (Union[Unset, str]): Specify a time duration in milliseconds,
            seconds, minutes, hours.
    """

    authorization_code_grant_access_token_lifespan: Union[Unset, str] = UNSET
    authorization_code_grant_id_token_lifespan: Union[Unset, str] = UNSET
    authorization_code_grant_refresh_token_lifespan: Union[Unset, str] = UNSET
    client_credentials_grant_access_token_lifespan: Union[Unset, str] = UNSET
    implicit_grant_access_token_lifespan: Union[Unset, str] = UNSET
    implicit_grant_id_token_lifespan: Union[Unset, str] = UNSET
    jwt_bearer_grant_access_token_lifespan: Union[Unset, str] = UNSET
    refresh_token_grant_access_token_lifespan: Union[Unset, str] = UNSET
    refresh_token_grant_id_token_lifespan: Union[Unset, str] = UNSET
    refresh_token_grant_refresh_token_lifespan: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        authorization_code_grant_access_token_lifespan = self.authorization_code_grant_access_token_lifespan
        authorization_code_grant_id_token_lifespan = self.authorization_code_grant_id_token_lifespan
        authorization_code_grant_refresh_token_lifespan = self.authorization_code_grant_refresh_token_lifespan
        client_credentials_grant_access_token_lifespan = self.client_credentials_grant_access_token_lifespan
        implicit_grant_access_token_lifespan = self.implicit_grant_access_token_lifespan
        implicit_grant_id_token_lifespan = self.implicit_grant_id_token_lifespan
        jwt_bearer_grant_access_token_lifespan = self.jwt_bearer_grant_access_token_lifespan
        refresh_token_grant_access_token_lifespan = self.refresh_token_grant_access_token_lifespan
        refresh_token_grant_id_token_lifespan = self.refresh_token_grant_id_token_lifespan
        refresh_token_grant_refresh_token_lifespan = self.refresh_token_grant_refresh_token_lifespan

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if authorization_code_grant_access_token_lifespan is not UNSET:
            field_dict["authorization_code_grant_access_token_lifespan"] = authorization_code_grant_access_token_lifespan
        if authorization_code_grant_id_token_lifespan is not UNSET:
            field_dict["authorization_code_grant_id_token_lifespan"] = authorization_code_grant_id_token_lifespan
        if authorization_code_grant_refresh_token_lifespan is not UNSET:
            field_dict["authorization_code_grant_refresh_token_lifespan"] = authorization_code_grant_refresh_token_lifespan
        if client_credentials_grant_access_token_lifespan is not UNSET:
            field_dict["client_credentials_grant_access_token_lifespan"] = client_credentials_grant_access_token_lifespan
        if implicit_grant_access_token_lifespan is not UNSET:
            field_dict["implicit_grant_access_token_lifespan"] = implicit_grant_access_token_lifespan
        if implicit_grant_id_token_lifespan is not UNSET:
            field_dict["implicit_grant_id_token_lifespan"] = implicit_grant_id_token_lifespan
        if jwt_bearer_grant_access_token_lifespan is not UNSET:
            field_dict["jwt_bearer_grant_access_token_lifespan"] = jwt_bearer_grant_access_token_lifespan
        if refresh_token_grant_access_token_lifespan is not UNSET:
            field_dict["refresh_token_grant_access_token_lifespan"] = refresh_token_grant_access_token_lifespan
        if refresh_token_grant_id_token_lifespan is not UNSET:
            field_dict["refresh_token_grant_id_token_lifespan"] = refresh_token_grant_id_token_lifespan
        if refresh_token_grant_refresh_token_lifespan is not UNSET:
            field_dict["refresh_token_grant_refresh_token_lifespan"] = refresh_token_grant_refresh_token_lifespan

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        authorization_code_grant_access_token_lifespan = _d.pop("authorization_code_grant_access_token_lifespan", UNSET)

        authorization_code_grant_id_token_lifespan = _d.pop("authorization_code_grant_id_token_lifespan", UNSET)

        authorization_code_grant_refresh_token_lifespan = _d.pop("authorization_code_grant_refresh_token_lifespan", UNSET)

        client_credentials_grant_access_token_lifespan = _d.pop("client_credentials_grant_access_token_lifespan", UNSET)

        implicit_grant_access_token_lifespan = _d.pop("implicit_grant_access_token_lifespan", UNSET)

        implicit_grant_id_token_lifespan = _d.pop("implicit_grant_id_token_lifespan", UNSET)

        jwt_bearer_grant_access_token_lifespan = _d.pop("jwt_bearer_grant_access_token_lifespan", UNSET)

        refresh_token_grant_access_token_lifespan = _d.pop("refresh_token_grant_access_token_lifespan", UNSET)

        refresh_token_grant_id_token_lifespan = _d.pop("refresh_token_grant_id_token_lifespan", UNSET)

        refresh_token_grant_refresh_token_lifespan = _d.pop("refresh_token_grant_refresh_token_lifespan", UNSET)

        o_auth_20_client_token_lifespans = cls(
            authorization_code_grant_access_token_lifespan=authorization_code_grant_access_token_lifespan,
            authorization_code_grant_id_token_lifespan=authorization_code_grant_id_token_lifespan,
            authorization_code_grant_refresh_token_lifespan=authorization_code_grant_refresh_token_lifespan,
            client_credentials_grant_access_token_lifespan=client_credentials_grant_access_token_lifespan,
            implicit_grant_access_token_lifespan=implicit_grant_access_token_lifespan,
            implicit_grant_id_token_lifespan=implicit_grant_id_token_lifespan,
            jwt_bearer_grant_access_token_lifespan=jwt_bearer_grant_access_token_lifespan,
            refresh_token_grant_access_token_lifespan=refresh_token_grant_access_token_lifespan,
            refresh_token_grant_id_token_lifespan=refresh_token_grant_id_token_lifespan,
            refresh_token_grant_refresh_token_lifespan=refresh_token_grant_refresh_token_lifespan,
        )

        o_auth_20_client_token_lifespans.additional_properties = _d
        return o_auth_20_client_token_lifespans

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
