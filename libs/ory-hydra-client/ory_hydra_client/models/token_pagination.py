from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union





T = TypeVar("T", bound="TokenPagination")

@attr.s(auto_attribs=True)
class TokenPagination:
    """
    Attributes:
        page_size (Union[Unset, int]): Items per page

            This is the number of items per page to return.
            For details on pagination please head over to the [pagination
            documentation](https://www.ory.sh/docs/ecosystem/api-design#pagination). Default: 250.
        page_token (Union[Unset, str]): Next Page Token

            The next page token.
            For details on pagination please head over to the [pagination
            documentation](https://www.ory.sh/docs/ecosystem/api-design#pagination). Default: '1'.
    """

    page_size: Union[Unset, int] = 250
    page_token: Union[Unset, str] = '1'
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        page_size = self.page_size
        page_token = self.page_token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if page_size is not UNSET:
            field_dict["page_size"] = page_size
        if page_token is not UNSET:
            field_dict["page_token"] = page_token

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        page_size = _d.pop("page_size", UNSET)

        page_token = _d.pop("page_token", UNSET)

        token_pagination = cls(
            page_size=page_size,
            page_token=page_token,
        )

        token_pagination.additional_properties = _d
        return token_pagination

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
