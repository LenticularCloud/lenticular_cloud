from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="PluginConfigArgs")


@attr.s(auto_attribs=True)
class PluginConfigArgs:
    """PluginConfigArgs plugin config args

    Attributes:
        description (str): description
        name (str): name
        settable (List[str]): settable
        value (List[str]): value
    """

    description: str
    name: str
    settable: List[str]
    value: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        settable = self.settable

        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Description": description,
                "Name": name,
                "Settable": settable,
                "Value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        description = _d.pop("Description")

        name = _d.pop("Name")

        settable = cast(List[str], _d.pop("Settable"))

        value = cast(List[str], _d.pop("Value"))

        plugin_config_args = cls(
            description=description,
            name=name,
            settable=settable,
            value=value,
        )

        plugin_config_args.additional_properties = _d
        return plugin_config_args

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
