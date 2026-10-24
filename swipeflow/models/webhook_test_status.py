from enum import StrEnum


class WebhookTestStatus(StrEnum):
    FAILED = "failed"
    QUEUED = "queued"
    SUCCEEDED = "succeeded"

    def __str__(self) -> str:
        return str(self.value)
