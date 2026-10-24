from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_status import WebhookDeliveryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayDeliveriesRequest")


@_attrs_define
class ReplayDeliveriesRequest:
    """
    Attributes:
        status (WebhookDeliveryStatus | Unset): Lifecycle state of one delivery. `held` = suspended mid-flight,
            resumable via reactivate. `cancelled` = permanent (webhook disabled or the source event expired). `dead` =
            retries exhausted, abandoned. Example: succeeded.
        since (datetime.datetime | Unset): Only replay deliveries created at or after this time
    """

    status: WebhookDeliveryStatus | Unset = UNSET
    since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: WebhookDeliveryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookDeliveryStatus(_status)

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        replay_deliveries_request = cls(
            status=status,
            since=since,
        )

        replay_deliveries_request.additional_properties = d
        return replay_deliveries_request

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
