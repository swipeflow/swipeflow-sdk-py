from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_delivery_status import WebhookDeliveryStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.delivery_error_type_0 import DeliveryErrorType0
    from ..models.webhook_delivery_attempt import WebhookDeliveryAttempt


T = TypeVar("T", bound="WebhookDeliveryDetail")


@_attrs_define
class WebhookDeliveryDetail:
    """
    Attributes:
        id (str | Unset):  Example: 0192f1a4-7c3e-7507-9f1f-6cd799439011.
        webhook_id (str | Unset):  Example: 0192f1a4-7c3e-7507-9f1f-6cd799439012.
        event_id (str | Unset): Public event id Example: evt_0192f1a4-7c3e-7507-9f1f-6cd799439013.
        event_type (str | Unset):  Example: item.approved.
        status (WebhookDeliveryStatus | Unset): Lifecycle state of one delivery. `held` = suspended mid-flight,
            resumable via reactivate. `cancelled` = permanent (webhook disabled or the source event expired). `dead` =
            retries exhausted, abandoned. Example: succeeded.
        attempts (int | Unset):  Example: 2.
        replay_of (None | str | Unset): The delivery this one replays, when it is a replay
        last_error (DeliveryErrorType0 | None | Unset):
        created_at (datetime.datetime | Unset):
        finished_at (datetime.datetime | None | Unset):
        attempts_list (list[WebhookDeliveryAttempt] | Unset):
        payload (Any | Unset): The source event's data — the request body this delivery sends
    """

    id: str | Unset = UNSET
    webhook_id: str | Unset = UNSET
    event_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    status: WebhookDeliveryStatus | Unset = UNSET
    attempts: int | Unset = UNSET
    replay_of: None | str | Unset = UNSET
    last_error: DeliveryErrorType0 | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    attempts_list: list[WebhookDeliveryAttempt] | Unset = UNSET
    payload: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.delivery_error_type_0 import DeliveryErrorType0

        id = self.id

        webhook_id = self.webhook_id

        event_id = self.event_id

        event_type = self.event_type

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        attempts = self.attempts

        replay_of: None | str | Unset
        if isinstance(self.replay_of, Unset):
            replay_of = UNSET
        else:
            replay_of = self.replay_of

        last_error: dict[str, Any] | None | Unset
        if isinstance(self.last_error, Unset):
            last_error = UNSET
        elif isinstance(self.last_error, DeliveryErrorType0):
            last_error = self.last_error.to_dict()
        else:
            last_error = self.last_error

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        attempts_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attempts_list, Unset):
            attempts_list = []
            for attempts_list_item_data in self.attempts_list:
                attempts_list_item = attempts_list_item_data.to_dict()
                attempts_list.append(attempts_list_item)

        payload = self.payload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if status is not UNSET:
            field_dict["status"] = status
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if replay_of is not UNSET:
            field_dict["replayOf"] = replay_of
        if last_error is not UNSET:
            field_dict["lastError"] = last_error
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if attempts_list is not UNSET:
            field_dict["attemptsList"] = attempts_list
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.delivery_error_type_0 import DeliveryErrorType0
        from ..models.webhook_delivery_attempt import WebhookDeliveryAttempt

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        webhook_id = d.pop("webhookId", UNSET)

        event_id = d.pop("eventId", UNSET)

        event_type = d.pop("eventType", UNSET)

        _status = d.pop("status", UNSET)
        status: WebhookDeliveryStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookDeliveryStatus(_status)

        attempts = d.pop("attempts", UNSET)

        def _parse_replay_of(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        replay_of = _parse_replay_of(d.pop("replayOf", UNSET))

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

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = datetime.datetime.fromisoformat(data)

                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))

        _attempts_list = d.pop("attemptsList", UNSET)
        attempts_list: list[WebhookDeliveryAttempt] | Unset = UNSET
        if _attempts_list is not UNSET:
            attempts_list = []
            for attempts_list_item_data in _attempts_list:
                attempts_list_item = WebhookDeliveryAttempt.from_dict(
                    attempts_list_item_data
                )

                attempts_list.append(attempts_list_item)

        payload = d.pop("payload", UNSET)

        webhook_delivery_detail = cls(
            id=id,
            webhook_id=webhook_id,
            event_id=event_id,
            event_type=event_type,
            status=status,
            attempts=attempts,
            replay_of=replay_of,
            last_error=last_error,
            created_at=created_at,
            finished_at=finished_at,
            attempts_list=attempts_list,
            payload=payload,
        )

        webhook_delivery_detail.additional_properties = d
        return webhook_delivery_detail

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
