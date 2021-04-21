import os
from time import time

import sqlalchemy as sqla

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
