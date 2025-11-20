from db.models import News
from db.session import async_session, get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select


class NewsDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_news(self, image_name: str, title: str, body: str) -> News:
        new_news = News(
            image_name=image_name,
            title=title,
            body=body,
        )
        self.db_session.add(new_news)
        await self.db_session.flush()
        return new_news

    async def get_all_news(self) -> List[News]:
        result = await self.db_session.execute(select(News))
        return list(result.scalars().all())
