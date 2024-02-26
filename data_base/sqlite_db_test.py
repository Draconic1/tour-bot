from data_base import sqlite_db
import pytest


def test_throws():
    with pytest.raises(TypeError):
        sqlite_db.sql_start(None)


def test_start_successfully():
    base = sqlite_db.sql_start(':memory:')
    result = base.execute('SELECT count(name) FROM sqlite_master WHERE type=\'table\' AND name=\'menu\';').fetchone()
    assert 1 == result[0]

