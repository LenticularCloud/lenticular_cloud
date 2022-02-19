from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CompletedRequest")


@attr.s(auto_attribs=True)
class CompletedRequest:
    """
    Attributes:
        redirect_to (str): RedirectURL is the URL which you should redirect the user to once the authentication process
            is completed.
    """

    redirect_to: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        redirect_to = self.redirect_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redirect_to": redirect_to,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        redirect_to = _d.pop("redirect_to")

        completed_request = cls(
            redirect_to=redirect_to,
        )

        completed_request.additional_properties = _d
        return completed_request

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
