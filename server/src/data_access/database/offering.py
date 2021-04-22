from dataclasses import asdict
from typing import List, Optional, Tuple

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


class OfferingAudioFilters(TypedDict):
    lang: str
    min_quantity: Optional[float]
    max_quantity: Optional[float]
    category: str
    subcategory: str


def retrieve_offering_audios(
    filters: OfferingAudioFilters
) -> List[OfferingAudio]:

    params: OfferingAudioFilters = {
        'lang': filters['lang'],
        'category': filters['category'],
        'subcategory': filters['subcategory'],
        'min_quantity': filters.get('min_quantity', 0.0),
        'max_quantity': filters.get('max_quantity', 9999.0),
    }

    print(params)

    query = '''
    select *
    from offering_audio
    where offering_id in (
        select id
        from offering
        where quantity_kg >= :min_quantity
        and quantity_kg <= :max_quantity
        and category = lower(:category)
        and lower(subcategory) = lower(:subcategory)
    ) and lang = :lang;
    '''
    result = engine.execute(sqla.text(query), params).fetchall()
    return [from_result(a, OfferingAudio) for a in result]


def create_offering(offering: Offering):
    query = '''
    insert into offering (
        id,
        created_at,
        updated_at,
        user_account_id,
        category,
        subcategory,
        quantity_kg,
        price_per_kg_cfa_cents
    )
    values (
        :id,
        :created_at,
        :updated_at,
        :user_account_id,
        :category,
        :subcategory,
        :quantity_kg,
        :price_per_kg_cfa_cents
    )
    returning *;
    '''
    engine.execute(sqla.text(query), asdict(offering))
