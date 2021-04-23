from dataclasses import dataclass, fields
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
        # NOTE(andrea): we override base class method
        # in order to prevent password hash from being sent
        # out of the system
        out = {}
        for field in fields(self):
            if field.name != 'password':
                out[field.name] = getattr(self, field.name)
        return out
