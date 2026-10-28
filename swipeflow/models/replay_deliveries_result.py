from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReplayDeliveriesResult")


@_attrs_define
class ReplayDeliveriesResult:
    """
    Attributes:
        replayed_count (int | Unset):
        skipped_count (int | Unset): Candidates skipped because their source event has already expired
    """

    replayed_count: int | Unset = UNSET
    skipped_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replayed_count = self.replayed_count

        skipped_count = self.skipped_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if replayed_count is not UNSET:
            field_dict["replayedCount"] = replayed_count
        if skipped_count is not UNSET:
            field_dict["skippedCount"] = skipped_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        replayed_count = d.pop("replayedCount", UNSET)

        skipped_count = d.pop("skippedCount", UNSET)

        replay_deliveries_result = cls(
            replayed_count=replayed_count,
            skipped_count=skipped_count,
        )

        replay_deliveries_result.additional_properties = d
        return replay_deliveries_result

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
