from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="PaginationResponseHeader")

@attr.s(auto_attribs=True)
class PaginationResponseHeader:
    """The `Link` HTTP header contains multiple links (`first`, `next`, `last`, `previous`) formatted as:
`<https://{project-slug}.projects.oryapis.com/admin/clients?page_size={limit}&page_token={offset}>; rel="{page}"`

For details on pagination please head over to the [pagination documentation](https://www.ory.sh/docs/ecosystem/api-
design#pagination).

    Attributes:
        link (Union[Unset, str]): The Link HTTP Header

            The `Link` header contains a comma-delimited list of links to the following pages:

            first: The first page of results.
            next: The next page of results.
            prev: The previous page of results.
            last: The last page of results.

            Pages are omitted if they do not exist. For example, if there is no next page, the `next` link is omitted.
            Examples:

            </clients?page_size=5&page_token=0>; rel="first",</clients?page_size=5&page_token=15>;
            rel="next",</clients?page_size=5&page_token=5>; rel="prev",</clients?page_size=5&page_token=20>; rel="last"
        x_total_count (Union[Unset, int]): The X-Total-Count HTTP Header

            The `X-Total-Count` header contains the total number of items in the collection.
    """

    link: Union[Unset, str] = UNSET
    x_total_count: Union[Unset, int] = UNSET
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

        pagination_response_header = cls(
            link=link,
            x_total_count=x_total_count,
        )

        pagination_response_header.additional_properties = _d
        return pagination_response_header

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
