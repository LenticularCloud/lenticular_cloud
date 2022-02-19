from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.plugin_device import PluginDevice
from ..models.plugin_mount import PluginMount

T = TypeVar("T", bound="PluginSettings")


@attr.s(auto_attribs=True)
class PluginSettings:
    """
    Attributes:
        args (List[str]): args
        devices (List[PluginDevice]): devices
        env (List[str]): env
        mounts (List[PluginMount]): mounts
    """

    args: List[str]
    devices: List[PluginDevice]
    env: List[str]
    mounts: List[PluginMount]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        args = self.args

        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)

        env = self.env

        mounts = []
        for mounts_item_data in self.mounts:
            mounts_item = mounts_item_data.to_dict()

            mounts.append(mounts_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Args": args,
                "Devices": devices,
                "Env": env,
                "Mounts": mounts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        args = cast(List[str], _d.pop("Args"))

        devices = []
        _devices = _d.pop("Devices")
        for devices_item_data in _devices:
            devices_item = PluginDevice.from_dict(devices_item_data)

            devices.append(devices_item)

        env = cast(List[str], _d.pop("Env"))

        mounts = []
        _mounts = _d.pop("Mounts")
        for mounts_item_data in _mounts:
            mounts_item = PluginMount.from_dict(mounts_item_data)

            mounts.append(mounts_item)

        plugin_settings = cls(
            args=args,
            devices=devices,
            env=env,
            mounts=mounts,
        )

        plugin_settings.additional_properties = _d
        return plugin_settings

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
