import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="FlushInactiveOAuth2TokensRequest")


@attr.s(auto_attribs=True)
class FlushInactiveOAuth2TokensRequest:
    """
    Attributes:
        not_after (Union[Unset, datetime.datetime]): NotAfter sets after which point tokens should not be flushed. This
            is useful when you want to keep a history
            of recently issued tokens for auditing.
    """

    not_after: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        not_after: Union[Unset, str] = UNSET
        if not isinstance(self.not_after, Unset):
            not_after = self.not_after.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if not_after is not UNSET:
            field_dict["notAfter"] = not_after

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        _not_after = _d.pop("notAfter", UNSET)
        not_after: Union[Unset, datetime.datetime]
        if isinstance(_not_after, Unset):
            not_after = UNSET
        else:
            not_after = isoparse(_not_after)

        flush_inactive_o_auth_2_tokens_request = cls(
            not_after=not_after,
        )

        flush_inactive_o_auth_2_tokens_request.additional_properties = _d
        return flush_inactive_o_auth_2_tokens_request

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
