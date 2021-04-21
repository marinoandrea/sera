from typing import List, Tuple

import sqlalchemy as sqla
from src.data_access.database import engine
from src.entities import Offering, OfferingAudio
from typing_extensions import TypedDict

from .utils import from_result


class OfferingData(TypedDict):
    user_account_id: str
    category: str
    subcategory: str
    quantity_kg: float
    price_per_kg_cfa_cents: int


def retrieve_latest_offerings() -> Tuple[List[Offering], List[OfferingAudio]]:
    query = '''
    select *
    from offering o1
    where o1.created_at = (
        select max(created_at)
        from offering o2
        where o2.category = o1.category
        and o2.subcategory = o1.subcategory
        and o2.user_account_id = o1.user_account_id
    );
    '''
    offerings = engine.execute(sqla.text(query)).fetchall()

    query = '''
    select *
    from offering_audio
    where offering_id = any(:offering_ids);
    '''
    audios = engine.execute(
        sqla.text(query),
        {'offering_ids': list(
            map(lambda o: o['id'], offerings)  # type: ignore
        )}
    )\
        .fetchall()

    return (
        [from_result(o, Offering) for o in offerings],
        [from_result(a, OfferingAudio) for a in audios]
    )
