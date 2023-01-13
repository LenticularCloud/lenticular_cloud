from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="ErrorOAuth2")

@attr.s(auto_attribs=True)
class ErrorOAuth2:
    """Error

    Attributes:
        error (Union[Unset, str]): Error
        error_debug (Union[Unset, str]): Error Debug Information

            Only available in dev mode.
        error_description (Union[Unset, str]): Error Description
        error_hint (Union[Unset, str]): Error Hint

            Helps the user identify the error cause. Example: The redirect URL is not allowed..
        status_code (Union[Unset, int]): HTTP Status Code Example: 401.
    """

    error: Union[Unset, str] = UNSET
    error_debug: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    error_hint: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        error_debug = self.error_debug
        error_description = self.error_description
        error_hint = self.error_hint
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if error is not UNSET:
            field_dict["error"] = error
        if error_debug is not UNSET:
            field_dict["error_debug"] = error_debug
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if error_hint is not UNSET:
            field_dict["error_hint"] = error_hint
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        error = _d.pop("error", UNSET)

        error_debug = _d.pop("error_debug", UNSET)

        error_description = _d.pop("error_description", UNSET)

        error_hint = _d.pop("error_hint", UNSET)

        status_code = _d.pop("status_code", UNSET)

        error_o_auth_2 = cls(
            error=error,
            error_debug=error_debug,
            error_description=error_description,
            error_hint=error_hint,
            status_code=status_code,
        )

        error_o_auth_2.additional_properties = _d
        return error_o_auth_2

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
