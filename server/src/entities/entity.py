from dataclasses import dataclass, field, fields
from time import time

from cuid import cuid


@dataclass(eq=True)
class Entity:
    id: str = field(default=cuid(), init=False)
    created_at: int = field(default=int(time() * 1000), init=False)
    updated_at: int = field(default=int(time() * 1000), init=False)

    def to_json(self) -> dict:
        return {f: getattr(self, f) for f in fields(self)}  # type: ignore
