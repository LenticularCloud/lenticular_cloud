from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GenericError")


@attr.s(auto_attribs=True)
class GenericError:
    """Error responses are sent when an error (e.g. unauthorized, bad request, ...) occurred.

    Attributes:
        error (str): Name is the error name. Example: The requested resource could not be found.
        debug (Union[Unset, str]): Debug contains debug information. This is usually not available and has to be
            enabled. Example: The database adapter was unable to find the element.
        error_description (Union[Unset, str]): Description contains further information on the nature of the error.
            Example: Object with ID 12345 does not exist.
        status_code (Union[Unset, int]): Code represents the error status code (404, 403, 401, ...). Example: 404.
    """

    error: str
    debug: Union[Unset, str] = UNSET
    error_description: Union[Unset, str] = UNSET
    status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        debug = self.debug
        error_description = self.error_description
        status_code = self.status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug
        if error_description is not UNSET:
            field_dict["error_description"] = error_description
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        error = _d.pop("error")

        debug = _d.pop("debug", UNSET)

        error_description = _d.pop("error_description", UNSET)

        status_code = _d.pop("status_code", UNSET)

        generic_error = cls(
            error=error,
            debug=debug,
            error_description=error_description,
            status_code=status_code,
        )

        generic_error.additional_properties = _d
        return generic_error

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
