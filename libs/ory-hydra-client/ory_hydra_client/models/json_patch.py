from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="JsonPatch")

@attr.s(auto_attribs=True)
class JsonPatch:
    """A JSONPatch document as defined by RFC 6902

    Attributes:
        op (str): The operation to be performed. One of "add", "remove", "replace", "move", "copy", or "test". Example:
            replace.
        path (str): The path to the target path. Uses JSON pointer notation.

            Learn more [about JSON Pointers](https://datatracker.ietf.org/doc/html/rfc6901#section-5). Example: /name.
        from_ (Union[Unset, str]): This field is used together with operation "move" and uses JSON Pointer notation.

            Learn more [about JSON Pointers](https://datatracker.ietf.org/doc/html/rfc6901#section-5). Example: /name.
        value (Union[Unset, Any]): The value to be used within the operations.

            Learn more [about JSON Pointers](https://datatracker.ietf.org/doc/html/rfc6901#section-5). Example: foobar.
    """

    op: str
    path: str
    from_: Union[Unset, str] = UNSET
    value: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        op = self.op
        path = self.path
        from_ = self.from_
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "op": op,
            "path": path,
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        op = _d.pop("op")

        path = _d.pop("path")

        from_ = _d.pop("from", UNSET)

        value = _d.pop("value", UNSET)

        json_patch = cls(
            op=op,
            path=path,
            from_=from_,
            value=value,
        )

        json_patch.additional_properties = _d
        return json_patch

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
