from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast
from typing import cast, List
from typing import Dict




T = TypeVar("T", bound="PluginConfigLinux")

@attr.s(auto_attribs=True)
class PluginConfigLinux:
    """PluginConfigLinux plugin config linux

    Attributes:
        allow_all_devices (bool): allow all devices
        capabilities (List[str]): capabilities
        devices (List['PluginDevice']): devices
    """

    allow_all_devices: bool
    capabilities: List[str]
    devices: List['PluginDevice']
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        allow_all_devices = self.allow_all_devices
        capabilities = self.capabilities




        devices = []
        for devices_item_data in self.devices:
            devices_item = devices_item_data.to_dict()

            devices.append(devices_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "AllowAllDevices": allow_all_devices,
            "Capabilities": capabilities,
            "Devices": devices,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        allow_all_devices = _d.pop("AllowAllDevices")

        capabilities = cast(List[str], _d.pop("Capabilities"))


        devices = []
        _devices = _d.pop("Devices")
        for devices_item_data in (_devices):
            devices_item = PluginDevice.from_dict(devices_item_data)



            devices.append(devices_item)


        plugin_config_linux = cls(
            allow_all_devices=allow_all_devices,
            capabilities=capabilities,
            devices=devices,
        )

        plugin_config_linux.additional_properties = _d
        return plugin_config_linux

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
