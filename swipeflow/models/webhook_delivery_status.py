from enum import StrEnum


class WebhookDeliveryStatus(StrEnum):
    CANCELLED = "cancelled"
    DEAD = "dead"
    GONE = "gone"
    HELD = "held"
    QUEUED = "queued"
    REJECTED = "rejected"
    RETRYING = "retrying"
    RUNNING = "running"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
