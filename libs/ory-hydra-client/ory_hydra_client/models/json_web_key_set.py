from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union
from typing import cast
from typing import Dict
from typing import cast, List

if TYPE_CHECKING:
  from ..models.json_web_key import JsonWebKey




T = TypeVar("T", bound="JsonWebKeySet")

@attr.s(auto_attribs=True)
class JsonWebKeySet:
    """JSON Web Key Set

    Attributes:
        keys (Union[Unset, List['JsonWebKey']]): List of JSON Web Keys

            The value of the "keys" parameter is an array of JSON Web Key (JWK)
            values. By default, the order of the JWK values within the array does
            not imply an order of preference among them, although applications
            of JWK Sets can choose to assign a meaning to the order for their
            purposes, if desired.
    """

    keys: Union[Unset, List['JsonWebKey']] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        from ..models.json_web_key import JsonWebKey
        keys: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.keys, Unset):
            keys = []
            for keys_item_data in self.keys:
                keys_item = keys_item_data.to_dict()

                keys.append(keys_item)





        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if keys is not UNSET:
            field_dict["keys"] = keys

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.json_web_key import JsonWebKey
        _d = src_dict.copy()
        keys = []
        _keys = _d.pop("keys", UNSET)
        for keys_item_data in (_keys or []):
            keys_item = JsonWebKey.from_dict(keys_item_data)



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
