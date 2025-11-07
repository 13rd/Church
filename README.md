# For "create commit" in alembic
uv run alembic revision --autogenerate -m "commit message"

# For "Push commit" in alembic
uv run alembic upgrade heads
