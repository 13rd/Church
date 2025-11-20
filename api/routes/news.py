from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.news import ShowNews, NewsCreate
from db.dals.news import NewsDAL
from db.session import get_db


news_router = APIRouter()


async def _create_new_news(body: NewsCreate, db) -> ShowNews:
    async with db as session:
        async with session.begin():
            news_dal = NewsDAL(session)
            news = await news_dal.create_news(
                image_name=body.image_name,
                title=body.title,
                body=body.body,
            )
        return ShowNews(
            news_id=news.news_id,
            image_name=news.image_name,
            title=news.title,
            body=news.body,
            is_active=news.is_active,
        )


async def _get_all_news(db) -> List[ShowNews]:
    async with db as session:
        async with session.begin():
            news_dal = NewsDAL(session)
            result = list(await news_dal.get_all_news())
            return result


@news_router.post("/", response_model=ShowNews)
async def create_news(body: NewsCreate, db: AsyncSession = Depends(get_db)) -> ShowNews:
    return await _create_new_news(body, db)


@news_router.get("/", response_model=List[ShowNews])
async def get_news(db: AsyncSession = Depends(get_db)) -> List[ShowNews]:
    return await _get_all_news(db)
