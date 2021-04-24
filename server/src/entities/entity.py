from dataclasses import asdict, dataclass, field
from time import time
from uuid import uuid4


def get_timestamp() -> int:
    return int(time() * 1000)


@dataclass(eq=True)
class Entity:
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    created_at: int = field(default_factory=get_timestamp, init=False)
    updated_at: int = field(default_factory=get_timestamp, init=False)

    # NOTE(andrea): this method will be overwritten by
    # subclasses in case we need to obfuscate some fields
    # when returning data from the API. (e.g. password hash)
    def to_json(self) -> dict:
        return asdict(self)
