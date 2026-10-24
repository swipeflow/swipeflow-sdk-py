from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_test_status import WebhookTestStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookTest")


@_attrs_define
class WebhookTest:
    """
    Attributes:
        id (str | Unset):  Example: 0192f1a4-7c3e-7507-9f1f-6cd799439011.
        status (WebhookTestStatus | Unset):
        status_code (int | None | Unset): HTTP response status code, when the request reached the receiver
        latency_ms (int | None | Unset):
        error (None | str | Unset):
        response_snippet (None | str | Unset):
        completed_at (datetime.datetime | None | Unset):
    """

    id: str | Unset = UNSET
    status: WebhookTestStatus | Unset = UNSET
    status_code: int | None | Unset = UNSET
    latency_ms: int | None | Unset = UNSET
    error: None | str | Unset = UNSET
    response_snippet: None | str | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        latency_ms: int | None | Unset
        if isinstance(self.latency_ms, Unset):
            latency_ms = UNSET
        else:
            latency_ms = self.latency_ms

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

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if error is not UNSET:
            field_dict["error"] = error
        if response_snippet is not UNSET:
            field_dict["responseSnippet"] = response_snippet
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _status = d.pop("status", UNSET)
        status: WebhookTestStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WebhookTestStatus(_status)

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))

        def _parse_latency_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latency_ms = _parse_latency_ms(d.pop("latencyMs", UNSET))

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

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        webhook_test = cls(
            id=id,
            status=status,
            status_code=status_code,
            latency_ms=latency_ms,
            error=error,
            response_snippet=response_snippet,
            completed_at=completed_at,
        )

        webhook_test.additional_properties = d
        return webhook_test

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
