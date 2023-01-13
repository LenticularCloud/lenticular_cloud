from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="TokenPaginationHeaders")

@attr.s(auto_attribs=True)
class TokenPaginationHeaders:
    """
    Attributes:
        link (Union[Unset, str]): The link header contains pagination links.

            For details on pagination please head over to the [pagination
            documentation](https://www.ory.sh/docs/ecosystem/api-design#pagination).

            in: header
        x_total_count (Union[Unset, str]): The total number of clients.

            in: header
    """

    link: Union[Unset, str] = UNSET
    x_total_count: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        link = self.link
        x_total_count = self.x_total_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if link is not UNSET:
            field_dict["link"] = link
        if x_total_count is not UNSET:
            field_dict["x-total-count"] = x_total_count

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        link = _d.pop("link", UNSET)

        x_total_count = _d.pop("x-total-count", UNSET)

        token_pagination_headers = cls(
            link=link,
            x_total_count=x_total_count,
        )

        token_pagination_headers.additional_properties = _d
        return token_pagination_headers

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
