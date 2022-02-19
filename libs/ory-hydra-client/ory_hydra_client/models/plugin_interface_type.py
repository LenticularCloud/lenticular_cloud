from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PluginInterfaceType")


@attr.s(auto_attribs=True)
class PluginInterfaceType:
    """PluginInterfaceType plugin interface type

    Attributes:
        capability (str): capability
        prefix (str): prefix
        version (str): version
    """

    capability: str
    prefix: str
    version: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        capability = self.capability
        prefix = self.prefix
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Capability": capability,
                "Prefix": prefix,
                "Version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        capability = _d.pop("Capability")

        prefix = _d.pop("Prefix")

        version = _d.pop("Version")

        plugin_interface_type = cls(
            capability=capability,
            prefix=prefix,
            version=version,
        )

        plugin_interface_type.additional_properties = _d
        return plugin_interface_type

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
