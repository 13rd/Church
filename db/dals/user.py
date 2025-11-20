from db.models import User
from db.session import async_session, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select


class UserDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(
        self, name: str, surname: str, email: str
    ) -> User:
        new_user = User(
            name=name,
            surname=surname,
            email=email,
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_all_users(self) -> List[User]:
        result = await self.db_session.execute(select(User))
        return list(result.scalars().all())
