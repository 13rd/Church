from typing import Generator, Any
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient
import settings
from main import app
import os
import asyncio
from db.session import get_db
import asyncpg


test_engine = create_async_engine(settings.TEST_DATABASE_URL, future=True, echo=True)\

test_async_session = sessionmaker(
    test_engine, expire_on_commit=False, class_=AsyncSession)

CLEAN_TABLES = [
    "users",
    "news"
]


def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def run_migrations():
    os.system("uv run alembic migrations")
    os.system('uv run alembic --autogenerate -m "test running migrations"')
    os.system("uv run alembic upgrade heads")
