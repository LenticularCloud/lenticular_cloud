from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


import attr

from ..types import UNSET, Unset






T = TypeVar("T", bound="OAuth20RedirectBrowserTo")

@attr.s(auto_attribs=True)
class OAuth20RedirectBrowserTo:
    """Contains a redirect URL used to complete a login, consent, or logout request.

    Attributes:
        redirect_to (str): RedirectURL is the URL which you should redirect the user's browser to once the
            authentication process is completed.
    """

    redirect_to: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        redirect_to = self.redirect_to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "redirect_to": redirect_to,
        })

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        _d = src_dict.copy()
        redirect_to = _d.pop("redirect_to")

        o_auth_20_redirect_browser_to = cls(
            redirect_to=redirect_to,
        )

        o_auth_20_redirect_browser_to.additional_properties = _d
        return o_auth_20_redirect_browser_to

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
