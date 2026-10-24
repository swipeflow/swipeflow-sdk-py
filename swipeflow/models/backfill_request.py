from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackfillRequest")


@_attrs_define
class BackfillRequest:
    """
    Attributes:
        after (str | Unset): Public event id to backfill strictly after (exclusive). Typically the webhook's
            reconciliation cursor. Example: evt_0192f1a4-7c3e-7507-9f1f-6cd799439013.
        since (datetime.datetime | Unset): Backfill events created at or after this time. Ignored when `after` is given.
    """

    after: str | Unset = UNSET
    since: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        since: str | Unset = UNSET
        if not isinstance(self.since, Unset):
            since = self.since.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if since is not UNSET:
            field_dict["since"] = since

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        _since = d.pop("since", UNSET)
        since: datetime.datetime | Unset
        if isinstance(_since, Unset):
            since = UNSET
        else:
            since = datetime.datetime.fromisoformat(_since)

        backfill_request = cls(
            after=after,
            since=since,
        )

        backfill_request.additional_properties = d
        return backfill_request

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
