from sqlalchemy.ext.asyncio import AsyncSession
from db.dals.news import NewsDAL
from api.schemas.news import NewsCreate, NewsUpdate, NewsResponse
from typing import Optional, List
from uuid import UUID

class NewsService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.dal = NewsDAL(db_session=db_session)

    async def create_news(self, news_data: NewsCreate) -> NewsResponse:
        news = await self.dal.create_news(news_data.model_dump())
        await self.db_session.commit()
        await self.db_session.refresh(news)

        return NewsResponse.model_validate(news)


    async def get_all_news(self, skip: int, limit: int) -> List[NewsResponse]:
        news_list = await self.dal.get_all_news(skip=skip, limit=limit, only_active=True)
        return [NewsResponse.model_validate(news) for news in news_list]


    async def get_news_by_id(self, news_id: str) -> Optional[NewsResponse]:
        news = await self.dal.get_news_by_id(news_id, only_active=True)
        if not news:
            return None
        return NewsResponse.model_validate(news)


    async def update_news(self, news_id: str, updated_data: NewsUpdate) -> Optional[NewsResponse]:
        updated_news = updated_data.model_dump()
        news = await self.dal.update_news(news_id, updated_news)
        if not news:
            return None

        await self.db_session.commit()
        await self.db_session.refresh(news)
        return NewsResponse.model_validate(news)


    async def delete_news(self, news_id: str) -> bool:
        result = await self.dal.delete_news(news_id)
        if result:
            await self.db_session.commit()
        return result