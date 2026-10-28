from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_error_type_0 import DeliveryErrorType0


T = TypeVar("T", bound="WebhookDeliveryHealth")


@_attrs_define
class WebhookDeliveryHealth:
    """System-owned delivery health, separate from the user-set `active` toggle.

    Attributes:
        active (bool | Unset): false means deliveries are suspended (sustained failure rate); reactivate to resume
            Example: True.
        suspended_at (datetime.datetime | None | Unset):
        reason (None | str | Unset):  Example: failure_rate.
        last_error (DeliveryErrorType0 | None | Unset):
    """

    active: bool | Unset = UNSET
    suspended_at: datetime.datetime | None | Unset = UNSET
    reason: None | str | Unset = UNSET
    last_error: DeliveryErrorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_error_type_0 import DeliveryErrorType0

        active = self.active

        suspended_at: None | str | Unset
        if isinstance(self.suspended_at, Unset):
            suspended_at = UNSET
        elif isinstance(self.suspended_at, datetime.datetime):
            suspended_at = self.suspended_at.isoformat()
        else:
            suspended_at = self.suspended_at

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        last_error: dict[str, Any] | None | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        elif isinstance(self.last_error, DeliveryErrorType0):
            last_error = self.last_error.to_dict()
        else:
            last_error = self.last_error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if suspended_at is not UNSET:
            field_dict["suspendedAt"] = suspended_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if last_error is not UNSET:
            field_dict["lastError"] = last_error

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.delivery_error_type_0 import DeliveryErrorType0

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        def _parse_suspended_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                suspended_at_type_0 = datetime.datetime.fromisoformat(data)

                return suspended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        suspended_at = _parse_suspended_at(d.pop("suspendedAt", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_last_error(data: object) -> DeliveryErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_delivery_error_type_0 = DeliveryErrorType0.from_dict(
                    data
                )

                return componentsschemas_delivery_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeliveryErrorType0 | None | Unset, data)

        last_error = _parse_last_error(d.pop("lastError", UNSET))

        webhook_delivery_health = cls(
            active=active,
            suspended_at=suspended_at,
            reason=reason,
            last_error=last_error,
        )

        webhook_delivery_health.additional_properties = d
        return webhook_delivery_health

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
