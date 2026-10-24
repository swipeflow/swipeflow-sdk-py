from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookDeliveryAttempt")


@_attrs_define
class WebhookDeliveryAttempt:
    """
    Attributes:
        id (str | Unset):  Example: 0192f1a4-7c3e-7507-9f1f-6cd799439011.
        n (int | Unset): Attempt number, 1-based Example: 1.
        at (datetime.datetime | Unset):
        latency_ms (int | None | Unset):
        status (int | None | Unset): HTTP response status code, when the request reached the receiver
        success (bool | Unset):
        category (None | str | Unset):
        error (None | str | Unset):
        response_snippet (None | str | Unset):
    """

    id: str | Unset = UNSET
    n: int | Unset = UNSET
    at: datetime.datetime | Unset = UNSET
    latency_ms: int | None | Unset = UNSET
    status: int | None | Unset = UNSET
    success: bool | Unset = UNSET
    category: None | str | Unset = UNSET
    error: None | str | Unset = UNSET
    response_snippet: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        n = self.n

        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        latency_ms: int | None | Unset
        if isinstance(self.latency_ms, Unset):
            latency_ms = UNSET
        else:
            latency_ms = self.latency_ms

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        success = self.success

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        response_snippet: None | str | Unset
        if isinstance(self.response_snippet, Unset):
            response_snippet = UNSET
        else:
            response_snippet = self.response_snippet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if n is not UNSET:
            field_dict["n"] = n
        if at is not UNSET:
            field_dict["at"] = at
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if status is not UNSET:
            field_dict["status"] = status
        if success is not UNSET:
            field_dict["success"] = success
        if category is not UNSET:
            field_dict["category"] = category
        if error is not UNSET:
            field_dict["error"] = error
        if response_snippet is not UNSET:
            field_dict["responseSnippet"] = response_snippet

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        n = d.pop("n", UNSET)

        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at, Unset):
            at = UNSET
        else:
            at = datetime.datetime.fromisoformat(_at)

        def _parse_latency_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latency_ms = _parse_latency_ms(d.pop("latencyMs", UNSET))

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        success = d.pop("success", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_response_snippet(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_snippet = _parse_response_snippet(d.pop("responseSnippet", UNSET))

        webhook_delivery_attempt = cls(
            id=id,
            n=n,
            at=at,
            latency_ms=latency_ms,
            status=status,
            success=success,
            category=category,
            error=error,
            response_snippet=response_snippet,
        )

        webhook_delivery_attempt.additional_properties = d
        return webhook_delivery_attempt

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
