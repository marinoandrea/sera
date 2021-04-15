from dataclasses import dataclass
from typing import Any, Optional


@dataclass(frozen=True, eq=True)
class HTTPRequest:
    resource: str
    method: str
    body: dict
    args: dict
    form: dict
    headers: dict


@dataclass(frozen=True, eq=True)
class HTTPResponse:
    status: int
    body: Optional[Any]
