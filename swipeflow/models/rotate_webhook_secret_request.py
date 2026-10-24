from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RotateWebhookSecretRequest")


@_attrs_define
class RotateWebhookSecretRequest:
    """
    Attributes:
        secret (str | Unset): Custom secret to rotate in. A cryptographically random one is generated when omitted.
        grace_period_seconds (int | Unset): How long the previous secret keeps signing alongside the new one (as
            `X-Swipeflow-Signature-Previous`). 0 rotates immediately with no grace window. Default: 86400. Example: 86400.
    """

    secret: str | Unset = UNSET
    grace_period_seconds: int | Unset = 86400
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        grace_period_seconds = self.grace_period_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret is not UNSET:
            field_dict["secret"] = secret
        if grace_period_seconds is not UNSET:
            field_dict["gracePeriodSeconds"] = grace_period_seconds

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret", UNSET)

        grace_period_seconds = d.pop("gracePeriodSeconds", UNSET)

        rotate_webhook_secret_request = cls(
            secret=secret,
            grace_period_seconds=grace_period_seconds,
        )

        rotate_webhook_secret_request.additional_properties = d
        return rotate_webhook_secret_request

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
