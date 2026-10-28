from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delivery_error_type_0_kind import DeliveryErrorType0Kind
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeliveryErrorType0")


@_attrs_define
class DeliveryErrorType0:
    """
    Attributes:
        kind (DeliveryErrorType0Kind | Unset):
        category (str | Unset):  Example: http_5xx.
        status (int | None | Unset):  Example: 503.
        message (None | str | Unset):
    """

    kind: DeliveryErrorType0Kind | Unset = UNSET
    category: str | Unset = UNSET
    status: int | None | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        category = self.category

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if kind is not UNSET:
            field_dict["kind"] = kind
        if category is not UNSET:
            field_dict["category"] = category
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: DeliveryErrorType0Kind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = DeliveryErrorType0Kind(_kind)

        category = d.pop("category", UNSET)

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        delivery_error_type_0 = cls(
            kind=kind,
            category=category,
            status=status,
            message=message,
        )

        delivery_error_type_0.additional_properties = d
        return delivery_error_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
