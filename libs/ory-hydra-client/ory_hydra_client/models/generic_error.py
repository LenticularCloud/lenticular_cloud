from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="GenericError")

@attr.s(auto_attribs=True)
class GenericError:
    """
    Attributes:
        message (str): Error message

            The error's message. Example: The resource could not be found.
        code (Union[Unset, int]): The status code Example: 404.
        debug (Union[Unset, str]): Debug information

            This field is often not exposed to protect against leaking
            sensitive information. Example: SQL field "foo" is not a bool..
        details (Union[Unset, Any]): Further error details
        id (Union[Unset, str]): The error ID

            Useful when trying to identify various errors in application logic.
        reason (Union[Unset, str]): A human-readable reason for the error Example: User with ID 1234 does not exist..
        request (Union[Unset, str]): The request ID

            The request ID is often exposed internally in order to trace
            errors across service architectures. This is often a UUID. Example: d7ef54b1-ec15-46e6-bccb-524b82c035e6.
        status (Union[Unset, str]): The status description Example: Not Found.
    """

    message: str
    code: Union[Unset, int] = UNSET
    debug: Union[Unset, str] = UNSET
    details: Union[Unset, Any] = UNSET
    id: Union[Unset, str] = UNSET
    reason: Union[Unset, str] = UNSET
    request: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        code = self.code
        debug = self.debug
        details = self.details
        id = self.id
        reason = self.reason
        request = self.request
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
        })
        if code is not UNSET:
            field_dict["code"] = code
        if debug is not UNSET:
            field_dict["debug"] = debug
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if request is not UNSET:
            field_dict["request"] = request
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        message = _d.pop("message")

        code = _d.pop("code", UNSET)

        debug = _d.pop("debug", UNSET)

        details = _d.pop("details", UNSET)

        id = _d.pop("id", UNSET)

        reason = _d.pop("reason", UNSET)

        request = _d.pop("request", UNSET)

        status = _d.pop("status", UNSET)

        generic_error = cls(
            message=message,
            code=code,
            debug=debug,
            details=details,
            id=id,
            reason=reason,
            request=request,
            status=status,
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
