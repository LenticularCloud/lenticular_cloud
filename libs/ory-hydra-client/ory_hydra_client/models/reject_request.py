from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union




T = TypeVar("T", bound="RejectRequest")

@attr.s(auto_attribs=True)
class RejectRequest:
    """
    Attributes:
        error (Union[Unset, str]): The error should follow the OAuth2 error format (e.g. `invalid_request`,
            `login_required`).

            Defaults to `request_denied`.
        error_debug (Union[Unset, str]): Debug contains information to help resolve the problem as a developer. Usually
            not exposed
            to the public but only in the server logs.
        error_description (Union[Unset, str]): Description of the error in a human readable format.
        error_hint (Union[Unset, str]): Hint to help resolve the error.
        status_code (Union[Unset, int]): Represents the HTTP status code of the error (e.g. 401 or 403)

            Defaults to 400
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

        reject_request = cls(
            error=error,
            error_debug=error_debug,
            error_description=error_description,
            error_hint=error_hint,
            status_code=status_code,
        )

        reject_request.additional_properties = _d
        return reject_request

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
