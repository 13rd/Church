from datetime import datetime

from db.models import News
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from sqlalchemy import select


class NewsDAL:
    """Data Access Layer for operating user info"""

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_news(self, news_data: dict) -> News:
        new_news = News(**news_data)
        self.db_session.add(new_news)
        return new_news

    async def get_all_news(self,
                           skip: int = 0,
                           limit: int = 10,
                           only_active: bool = True) -> List[News]:
        query = select(News)
        if only_active:
            query = query.where(News.is_active == True)

        query = query.order_by(News.created_at.desc())
        query = query.offset(skip).limit(limit)

        result = await self.db_session.execute(query)
        return list(result.scalars().all())


    async def get_news_by_id(self, news_id: str, only_active: bool = True) -> Optional[News]:
        query = select(News).where(News.news_id == news_id)
        if only_active:
            query = query.where(News.is_active == True)

        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()


    async def update_news(self, news_id: str, update_data: dict) -> Optional[News]:
        news = await self.get_news_by_id(news_id, only_active=False)
        if not news:
            return None

        for key, value in update_data.items():
            if value is not None:
                setattr(news, key, value)

        news.updated_at = datetime.now()
        return news


    async def delete_news(self, news_id: str) -> bool:
        news = await self.get_news_by_id(news_id, only_active=False)
        if not news:
            return False
        news.is_active = False
        return True