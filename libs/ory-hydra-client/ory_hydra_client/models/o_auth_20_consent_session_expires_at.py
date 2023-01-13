from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union
from dateutil.parser import isoparse
import datetime





T = TypeVar("T", bound="OAuth20ConsentSessionExpiresAt")

@attr.s(auto_attribs=True)
class OAuth20ConsentSessionExpiresAt:
    """
    Attributes:
        access_token (Union[Unset, datetime.datetime]):
        authorize_code (Union[Unset, datetime.datetime]):
        id_token (Union[Unset, datetime.datetime]):
        par_context (Union[Unset, datetime.datetime]):
        refresh_token (Union[Unset, datetime.datetime]):
    """

    access_token: Union[Unset, datetime.datetime] = UNSET
    authorize_code: Union[Unset, datetime.datetime] = UNSET
    id_token: Union[Unset, datetime.datetime] = UNSET
    par_context: Union[Unset, datetime.datetime] = UNSET
    refresh_token: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        access_token: Union[Unset, str] = UNSET
        if not isinstance(self.access_token, Unset):
            access_token = self.access_token.isoformat()

        authorize_code: Union[Unset, str] = UNSET
        if not isinstance(self.authorize_code, Unset):
            authorize_code = self.authorize_code.isoformat()

        id_token: Union[Unset, str] = UNSET
        if not isinstance(self.id_token, Unset):
            id_token = self.id_token.isoformat()

        par_context: Union[Unset, str] = UNSET
        if not isinstance(self.par_context, Unset):
            par_context = self.par_context.isoformat()

        refresh_token: Union[Unset, str] = UNSET
        if not isinstance(self.refresh_token, Unset):
            refresh_token = self.refresh_token.isoformat()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_token is not UNSET:
            field_dict["access_token"] = access_token
        if authorize_code is not UNSET:
            field_dict["authorize_code"] = authorize_code
        if id_token is not UNSET:
            field_dict["id_token"] = id_token
        if par_context is not UNSET:
            field_dict["par_context"] = par_context
        if refresh_token is not UNSET:
            field_dict["refresh_token"] = refresh_token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        _access_token = _d.pop("access_token", UNSET)
        access_token: Union[Unset, datetime.datetime]
        if isinstance(_access_token,  Unset):
            access_token = UNSET
        else:
            access_token = isoparse(_access_token)




        _authorize_code = _d.pop("authorize_code", UNSET)
        authorize_code: Union[Unset, datetime.datetime]
        if isinstance(_authorize_code,  Unset):
            authorize_code = UNSET
        else:
            authorize_code = isoparse(_authorize_code)




        _id_token = _d.pop("id_token", UNSET)
        id_token: Union[Unset, datetime.datetime]
        if isinstance(_id_token,  Unset):
            id_token = UNSET
        else:
            id_token = isoparse(_id_token)




        _par_context = _d.pop("par_context", UNSET)
        par_context: Union[Unset, datetime.datetime]
        if isinstance(_par_context,  Unset):
            par_context = UNSET
        else:
            par_context = isoparse(_par_context)




        _refresh_token = _d.pop("refresh_token", UNSET)
        refresh_token: Union[Unset, datetime.datetime]
        if isinstance(_refresh_token,  Unset):
            refresh_token = UNSET
        else:
            refresh_token = isoparse(_refresh_token)




        o_auth_20_consent_session_expires_at = cls(
            access_token=access_token,
            authorize_code=authorize_code,
            id_token=id_token,
            par_context=par_context,
            refresh_token=refresh_token,
        )

        o_auth_20_consent_session_expires_at.additional_properties = _d
        return o_auth_20_consent_session_expires_at

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
