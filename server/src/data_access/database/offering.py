from typing import List

import sqlalchemy as sqla
from src.data_access.database import engine
from src.entities import Offering
from typing_extensions import TypedDict


class OfferingData(TypedDict):
    Offering_account_id: str
    category: str
    subcategory: str
    quantity_kg: float
    price_per_kg_cfa_cents: int
    audio_asset: str


def from_result(result: dict) -> Offering:
    # NOTE(andrea): this is a workaround
    # for having default fields in the base
    # Entity class. Dataclasses do not allow
    # to use defaulted fields in the __init__,
    # we therefore have to set these fields
    # explicitly.
    out = Offering(**result)
    out.id = result['id']
    out.created_at = result['created_at']
    out.updated_at = result['updated_at']
    return out


def retrieve_latest_offerings() -> List[Offering]:
    query = '''
    select *
    from offering
    where created_at = (
        select max(created_at)
        from offering
        group by user_account_id, category, subcategory
    );
    '''
    result = engine.execute(sqla.text(query)).fetchall()
    return [from_result(r) for r in result]