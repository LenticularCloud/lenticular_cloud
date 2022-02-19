from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.plugin_interface_type import PluginInterfaceType

T = TypeVar("T", bound="PluginConfigInterface")


@attr.s(auto_attribs=True)
class PluginConfigInterface:
    """PluginConfigInterface The interface between Docker and the plugin

    Attributes:
        socket (str): socket
        types (List[PluginInterfaceType]): types
    """

    socket: str
    types: List[PluginInterfaceType]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        socket = self.socket
        types = []
        for types_item_data in self.types:
            types_item = types_item_data.to_dict()

            types.append(types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Socket": socket,
                "Types": types,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        socket = _d.pop("Socket")

        types = []
        _types = _d.pop("Types")
        for types_item_data in _types:
            types_item = PluginInterfaceType.from_dict(types_item_data)

            types.append(types_item)

        plugin_config_interface = cls(
            socket=socket,
            types=types,
        )

        plugin_config_interface.additional_properties = _d
        return plugin_config_interface

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
