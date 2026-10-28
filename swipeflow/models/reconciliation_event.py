from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Self, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reconciliation_event_data import ReconciliationEventData


T = TypeVar("T", bound="ReconciliationEvent")


@_attrs_define
class ReconciliationEvent:
    """
    Attributes:
        id (str | Unset):  Example: evt_0192f1a4-7c3e-7507-9f1f-6cd799439013.
        type_ (str | Unset):  Example: item.approved.
        created_at (datetime.datetime | Unset):
        data (ReconciliationEventData | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    data: ReconciliationEventData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.reconciliation_event_data import ReconciliationEventData

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _data = d.pop("data", UNSET)
        data: ReconciliationEventData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ReconciliationEventData.from_dict(_data)

        reconciliation_event = cls(
            id=id,
            type_=type_,
            created_at=created_at,
            data=data,
        )

        reconciliation_event.additional_properties = d
        return reconciliation_event

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
