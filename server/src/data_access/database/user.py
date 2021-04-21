from dataclasses import asdict
from typing import Any, Mapping, Optional

import sqlalchemy as sqla
from src.data_access.database import engine, get_cursor
from src.entities import User
from typing_extensions import TypedDict

from .utils import from_result


class UserData(TypedDict):
    name: str
    user_group: str
    email: str
    phone_number: str
    is_admin: bool
    password: str


def retrieve_user_by_id(id: str) -> Optional[User]:
    query = '''
    select *
    from user_account
    where id = :id;
    '''
    result = engine.execute(sqla.text(query), {'id': id})\
        .first()
    return from_result(result, User) if result else None


def retrieve_user_by_phone_number(phone_number: str) -> Optional[User]:
    query = '''
    select *
    from user_account
    where phone_number = :phone_number;
    '''
    result = engine.execute(sqla.text(query), {'phone_number': phone_number})\
        .first()
    return from_result(result, User) if result else None


def create_user(data: User) -> User:
    query = '''
    insert into user_account (
        id,
        created_at,
        updated_at,
        name,
        user_group,
        email,
        phone_number,
        password
    )
    values (
        :id,
        :created_at,
        :updated_at,
        :name,
        :user_group,
        :email,
        :phone_number,
        :password,
    )
    returning *;
    '''
    result = engine.execute(sqla.text(query), asdict(data))\
        .first()
    return from_result(result, User)  # type: ignore


def delete_user(id: str):
    query = '''
    delete from user_account
    where id = :id;
    '''
    engine.execute(sqla.text(query), {'id': id})


def update_user(id: str, data: UserData) -> User:
    def _parse_args() -> str:
        out = ''
        if 'name' in data:
            out += 'name = :name,\n'
        if 'user_group' in data:
            out += 'user_group = :user_group,\n'
        if 'email' in data:
            out += 'email = :email,\n'
        if 'phone_number' in data:
            out += 'phone_number = :phone_number,\n'
        if 'is_admin' in data:
            out += 'is_admin = :is_admin,\n'
        if 'password' in data:
            out += 'password = :password,\n'
        return out

    query = f'''
    update user_account
    set {_parse_args()}
    updated_at = :updated_at
    where id = :id
    returning *;
    '''

    params: Mapping[str, Any] = {**data, 'updated_at': get_cursor()}

    result = engine.execute(sqla.text(query), params)\
        .first()

    return from_result(result, User)  # type: ignore
