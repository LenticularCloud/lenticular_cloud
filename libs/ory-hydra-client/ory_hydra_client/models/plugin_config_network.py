from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PluginConfigNetwork")


@attr.s(auto_attribs=True)
class PluginConfigNetwork:
    """PluginConfigNetwork plugin config network

    Attributes:
        type (str): type
    """

    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        type = _d.pop("Type")

        plugin_config_network = cls(
            type=type,
        )

        plugin_config_network.additional_properties = _d
        return plugin_config_network

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
