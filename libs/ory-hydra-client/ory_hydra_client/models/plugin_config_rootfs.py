from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginConfigRootfs")


@attr.s(auto_attribs=True)
class PluginConfigRootfs:
    """PluginConfigRootfs plugin config rootfs

    Attributes:
        diff_ids (Union[Unset, List[str]]): diff ids
        type (Union[Unset, str]): type
    """

    diff_ids: Union[Unset, List[str]] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        diff_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.diff_ids, Unset):
            diff_ids = self.diff_ids

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if diff_ids is not UNSET:
            field_dict["diff_ids"] = diff_ids
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        diff_ids = cast(List[str], _d.pop("diff_ids", UNSET))

        type = _d.pop("type", UNSET)

        plugin_config_rootfs = cls(
            diff_ids=diff_ids,
            type=type,
        )

        plugin_config_rootfs.additional_properties = _d
        return plugin_config_rootfs

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
