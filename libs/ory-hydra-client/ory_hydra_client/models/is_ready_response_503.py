from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Dict
from typing import Union
from typing import cast

if TYPE_CHECKING:
  from ..models.is_ready_response_503_errors import IsReadyResponse503Errors




T = TypeVar("T", bound="IsReadyResponse503")

@attr.s(auto_attribs=True)
class IsReadyResponse503:
    """
    Attributes:
        errors (Union[Unset, IsReadyResponse503Errors]): Errors contains a list of errors that caused the not ready
            status.
    """

    errors: Union[Unset, 'IsReadyResponse503Errors'] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.is_ready_response_503_errors import IsReadyResponse503Errors
        errors: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.is_ready_response_503_errors import IsReadyResponse503Errors
        _d = src_dict.copy()
        _errors = _d.pop("errors", UNSET)
        errors: Union[Unset, IsReadyResponse503Errors]
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = IsReadyResponse503Errors.from_dict(_errors)




        is_ready_response_503 = cls(
            errors=errors,
        )

        is_ready_response_503.additional_properties = _d
        return is_ready_response_503

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
