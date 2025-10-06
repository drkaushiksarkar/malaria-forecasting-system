import pytest
from sqlalchemy.exc import OperationalError
from src.database.manager import get_engine

def test_engine_env_required(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(RuntimeError):
        get_engine()