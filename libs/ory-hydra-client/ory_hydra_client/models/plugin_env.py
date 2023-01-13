from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast, List




T = TypeVar("T", bound="PluginEnv")

@attr.s(auto_attribs=True)
class PluginEnv:
    """PluginEnv plugin env

    Attributes:
        description (str): description
        name (str): name
        settable (List[str]): settable
        value (str): value
    """

    description: str
    name: str
    settable: List[str]
    value: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        settable = self.settable




        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "Description": description,
            "Name": name,
            "Settable": settable,
            "Value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        description = _d.pop("Description")

        name = _d.pop("Name")

        settable = cast(List[str], _d.pop("Settable"))


        value = _d.pop("Value")

        plugin_env = cls(
            description=description,
            name=name,
            settable=settable,
            value=value,
        )

        plugin_env.additional_properties = _d
        return plugin_env

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
