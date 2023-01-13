from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset





T = TypeVar("T", bound="VolumeUsageData")

@attr.s(auto_attribs=True)
class VolumeUsageData:
    """VolumeUsageData Usage details about the volume. This information is used by the
`GET /system/df` endpoint, and omitted in other endpoints.

    Attributes:
        ref_count (int): The number of containers referencing this volume. This field
            is set to `-1` if the reference-count is not available.
        size (int): Amount of disk space used by the volume (in bytes). This information
            is only available for volumes created with the `"local"` volume
            driver. For volumes created with other volume drivers, this field
            is set to `-1` ("not available")
    """

    ref_count: int
    size: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        ref_count = self.ref_count
        size = self.size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "RefCount": ref_count,
            "Size": size,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        ref_count = _d.pop("RefCount")

        size = _d.pop("Size")

        volume_usage_data = cls(
            ref_count=ref_count,
            size=size,
        )

        volume_usage_data.additional_properties = _d
        return volume_usage_data

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
