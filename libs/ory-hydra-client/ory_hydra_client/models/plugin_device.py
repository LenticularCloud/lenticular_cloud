from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PluginDevice")


@attr.s(auto_attribs=True)
class PluginDevice:
    """PluginDevice plugin device

    Attributes:
        description (str): description
        name (str): name
        path (str): path
        settable (List[str]): settable
    """

    description: str
    name: str
    path: str
    settable: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        path = self.path
        settable = self.settable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Description": description,
                "Name": name,
                "Path": path,
                "Settable": settable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        description = _d.pop("Description")

        name = _d.pop("Name")

        path = _d.pop("Path")

        settable = cast(List[str], _d.pop("Settable"))

        plugin_device = cls(
            description=description,
            name=name,
            path=path,
            settable=settable,
        )

        plugin_device.additional_properties = _d
        return plugin_device

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
