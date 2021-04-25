import os
from functools import wraps
from time import time
from typing import Callable

import psycopg2
import sqlalchemy as sqla
from src.errors import DataAccessError, ValidationError

engine: sqla.engine.Engine = sqla.create_engine(
    os.getenv('DATABASE_URL', '').replace('postgres:/', 'postgresql:/'),
    echo=os.getenv('APP_ENVIRONMENT') == 'development',
    pool_size=10,
    max_overflow=10,
)


def with_transaction():
    connection = engine.connect()
    trans = connection.begin()
    try:
        yield trans
        trans.commit()
    except Exception as e:
        trans.rollback()
        raise e


def get_cursor() -> int:
    return int(time() * 1000)


def db_operation(f: Callable):

    @wraps(f)
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except sqla.exc.DBAPIError as e:

            if (isinstance(e.orig, psycopg2.errors.UniqueViolation)):
                column = e.diag.column_name
                raise ValidationError(
                    f'This value for \'{column}\' is already present.')

            # TODO(andrea): more exceptions should have custom handling

            raise DataAccessError from e
    return inner
