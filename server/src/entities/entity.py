from dataclasses import dataclass, field, fields
from time import time
from uuid import uuid4


@dataclass(eq=True)
class Entity:
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    created_at: int = field(default_factory=lambda: int(time() * 1000), init=False)
    updated_at: int = field(default_factory=lambda: int(time() * 1000), init=False)

    def to_json(self) -> dict:
        # type: ignore
        return {f.name: getattr(self, f.name) for f in fields(self)}
