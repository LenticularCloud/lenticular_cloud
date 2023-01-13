from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union




T = TypeVar("T", bound="Oauth2TokenData")

@attr.s(auto_attribs=True)
class Oauth2TokenData:
    """
    Attributes:
        grant_type (str):
        code (Union[Unset, str]):
        refresh_token (Union[Unset, str]):
        redirect_uri (Union[Unset, str]):
        client_id (Union[Unset, str]):
    """

    grant_type: str
    code: Union[Unset, str] = UNSET
    refresh_token: Union[Unset, str] = UNSET
    redirect_uri: Union[Unset, str] = UNSET
    client_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type
        code = self.code
        refresh_token = self.refresh_token
        redirect_uri = self.redirect_uri
        client_id = self.client_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "grant_type": grant_type,
        })
        if code is not UNSET:
            field_dict["code"] = code
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token
        if redirect_uri is not UNSET:
            field_dict["redirect_uri"] = redirect_uri
        if client_id is not UNSET:
            field_dict["client_id"] = client_id

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        grant_type = _d.pop("grant_type")

        code = _d.pop("code", UNSET)

        refresh_token = _d.pop("refresh_token", UNSET)

        redirect_uri = _d.pop("redirect_uri", UNSET)

        client_id = _d.pop("client_id", UNSET)

        oauth_2_token_data = cls(
            grant_type=grant_type,
            code=code,
            refresh_token=refresh_token,
            redirect_uri=redirect_uri,
            client_id=client_id,
        )

        oauth_2_token_data.additional_properties = _d
        return oauth_2_token_data

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
