from typing import Any, Mapping


def from_result(result: Mapping[str, Any], entity: type) -> Any:
    # NOTE(andrea): this is a workaround
    # for having default fields in the base
    # Entity class. Dataclasses do not allow
    # to use defaulted fields in the __init__,
    # we therefore have to set these fields
    # explicitly.
    result = dict(result)
    id = result.pop('id')
    created_at = result.pop('created_at')
    updated_at = result.pop('updated_at')
    out = entity(**result)
    out.id = id  # type: ignore
    out.created_at = created_at  # type: ignore
    out.updated_at = updated_at  # type: ignore
    return out
