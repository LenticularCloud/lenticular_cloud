from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.json_web_key import JSONWebKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="JSONWebKeySet")


@attr.s(auto_attribs=True)
class JSONWebKeySet:
    """It is important that this model object is named JSONWebKeySet for
    "swagger generate spec" to generate only on definition of a
    JSONWebKeySet. Since one with the same name is previously defined as
    client.Client.JSONWebKeys and this one is last, this one will be
    effectively written in the swagger spec.

        Attributes:
            keys (Union[Unset, List[JSONWebKey]]): The value of the "keys" parameter is an array of JWK values.  By
                default, the order of the JWK values within the array does not imply
                an order of preference among them, although applications of JWK Sets
                can choose to assign a meaning to the order for their purposes, if
                desired.
    """

    keys: Union[Unset, List[JSONWebKey]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()

                keys.append(keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        keys = []
        _keys = _d.pop("keys", UNSET)
        for keys_item_data in _keys or []:
            keys_item = JSONWebKey.from_dict(keys_item_data)

            keys.append(keys_item)

        json_web_key_set = cls(
            keys=keys,
        )

        json_web_key_set.additional_properties = _d
        return json_web_key_set

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
