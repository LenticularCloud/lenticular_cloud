from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginConfigUser")


@attr.s(auto_attribs=True)
class PluginConfigUser:
    """PluginConfigUser plugin config user

    Attributes:
        gid (Union[Unset, int]): g ID
        uid (Union[Unset, int]): UID
    """

    gid: Union[Unset, int] = UNSET
    uid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gid = self.gid
        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gid is not UNSET:
            field_dict["GID"] = gid
        if uid is not UNSET:
            field_dict["UID"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        gid = _d.pop("GID", UNSET)

        uid = _d.pop("UID", UNSET)

        plugin_config_user = cls(
            gid=gid,
            uid=uid,
        )

        plugin_config_user.additional_properties = _d
        return plugin_config_user

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
