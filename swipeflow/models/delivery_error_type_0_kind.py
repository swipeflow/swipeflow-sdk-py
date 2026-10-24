from enum import StrEnum


class DeliveryErrorType0Kind(StrEnum):
    PERMANENT = "permanent"
    TRANSIENT = "transient"

    def __str__(self) -> str:
        return str(self.value)
