from dataclasses import asdict, dataclass
from typing import Optional

from .entity import Entity


@dataclass
class User(Entity):
    name: str
    user_group: str
    email: str
    password: str
    phone_number: Optional[str] = None
    is_admin: bool = False

    def to_json(self) -> dict:
        out = asdict(self)
        out.pop('password')
        return out
