from dataclasses import asdict
from typing import List, Optional

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


def retrieve_latest_offerings() -> List[Offering]:
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
    return [from_result(o, Offering) for o in offerings]


def retrieve_offering_audios_by_id(ids: List[str]) -> List[OfferingAudio]:
    query = '''
    select *
    from offering_audio
    where offering_id = any(:ids);
    '''
    audios = engine.execute(sqla.text(query), {'ids': ids}).fetchall()
    return [from_result(a, OfferingAudio) for a in audios]


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


def create_offering_audio(offering_audio: OfferingAudio):
    query = '''
    insert into offering_audio (
        id,
        created_at,
        updated_at,
        offering_id,
        lang,
        path
    )
    values (
        :id,
        :created_at,
        :updated_at,
        :offering_id,
        :lang,
        :path
    )
    returning *;
    '''
    engine.execute(sqla.text(query), asdict(offering_audio))


class OfferingFilters(TypedDict):
    min_quantity: float
    max_quantity: float
    category: str
    subcategory: str


def retrieve_offerings(filters: OfferingFilters) -> List[Offering]:

    params: OfferingFilters = {
        'category': filters['category'],
        'subcategory': filters['subcategory'],
        'min_quantity': filters.get('min_quantity', 0.0),
        'max_quantity': filters.get('max_quantity', 9999.0),
    }

    query = '''
    select *
    from offering o1
    where o1.created_at = (
        select max(created_at)
        from offering o2
        where o2.category = o1.category
        and o2.subcategory = o1.subcategory
        and o2.user_account_id = o1.user_account_id
        and o1.category = :category
        and o1.subcategory = :subcategory
        and o1.quantity_kg >= :min_quantity
        and o1.quantity_kg <= :max_quantity
    );
    '''
    result = engine.execute(sqla.text(query), params).fetchall()

    return [from_result(a, Offering) for a in result]
