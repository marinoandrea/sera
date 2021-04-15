import os

import sqlalchemy as sqla

engine: sqla.engine.Engine = sqla.create_engine(
    os.getenv('DATABASE_URL'),
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
