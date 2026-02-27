from typing import List
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from api.schemas.news import NewsResponse, NewsCreate, NewsUpdate
from api.service.news import NewsService
from db.session import get_db


news_router = APIRouter(prefix="/news", tags=["News"])

def get_news_service(db: AsyncSession = Depends(get_db)) -> NewsService:
    return NewsService(db)

@news_router.post("/", response_model=NewsResponse, status_code=status.HTTP_201_CREATED)
async def create_news(news_data: NewsCreate,
                      service: NewsService = Depends(get_news_service)):
    return await service.create_news(news_data)


@news_router.get("/", response_model=List[NewsResponse], status_code=status.HTTP_200_OK)
async def get_all_news(skip: int = Query(0, ge=0),
                   limit: int = Query(10, ge=1, le=100),
                   service: NewsService = Depends(get_news_service)) -> List[NewsResponse]:
    return await service.get_all_news(skip, limit)


@news_router.get("/{news_id}", response_model=NewsResponse, status_code=status.HTTP_200_OK)
async def news_detail(news_id: str, service: NewsService = Depends(get_news_service)):
    news =  await service.get_news_by_id(news_id=news_id)
    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    return news


@news_router.patch("/{news_id}", response_model=NewsResponse, status_code=status.HTTP_200_OK)
async def update_news(news_id: str, news_data: NewsUpdate, service: NewsService = Depends(get_news_service)):
    news = await service.update_news(news_id, news_data)
    if not news:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    return news


@news_router.delete("/{news_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_news(news_id: str, service: NewsService = Depends(get_news_service)):
    success = await service.delete_news(news_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="News not found")
    return ...





