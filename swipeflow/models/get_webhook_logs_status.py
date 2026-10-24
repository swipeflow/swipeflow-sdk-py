from enum import StrEnum


class GetWebhookLogsStatus(StrEnum):
    FAILED = "failed"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
