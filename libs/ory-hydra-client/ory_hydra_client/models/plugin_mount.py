from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO

from typing import List


import attr

from ..types import UNSET, Unset

from typing import cast, List




T = TypeVar("T", bound="PluginMount")

@attr.s(auto_attribs=True)
class PluginMount:
    """PluginMount plugin mount

    Attributes:
        description (str): description
        destination (str): destination
        name (str): name
        options (List[str]): options
        settable (List[str]): settable
        source (str): source
        type (str): type
    """

    description: str
    destination: str
    name: str
    options: List[str]
    settable: List[str]
    source: str
    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        destination = self.destination
        name = self.name
        options = self.options




        settable = self.settable




        source = self.source
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "Description": description,
            "Destination": destination,
            "Name": name,
            "Options": options,
            "Settable": settable,
            "Source": source,
            "Type": type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        description = _d.pop("Description")

        destination = _d.pop("Destination")

        name = _d.pop("Name")

        options = cast(List[str], _d.pop("Options"))


        settable = cast(List[str], _d.pop("Settable"))


        source = _d.pop("Source")

        type = _d.pop("Type")

        plugin_mount = cls(
            description=description,
            destination=destination,
            name=name,
            options=options,
            settable=settable,
            source=source,
            type=type,
        )

        plugin_mount.additional_properties = _d
        return plugin_mount

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
