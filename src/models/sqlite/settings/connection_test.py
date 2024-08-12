import pytest
from sqlalchemy import Engine
from .connection import db_connection_handler


@pytest.mark.skip(reason="Integration to database")
def test_connection_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect_to_db()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
