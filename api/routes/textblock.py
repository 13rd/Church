from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from api.schemas.textblock import TextBlockResponse, TextBlockCreate, TextBlockUpdate
from api.service.textblock import TextblockService
from db.session import get_db

textblock_router = APIRouter(prefix="/textblock", tags=["Textblock"])

def get_textblock_service(db: AsyncSession = Depends(get_db)) -> TextblockService:
    return TextblockService(db)


@textblock_router.get("/", response_model=List[TextBlockResponse] , status_code=status.HTTP_200_OK)
async def get_all_textblocks(service: TextblockService = Depends(get_textblock_service)):
    return await service.get_all_textblocks()


@textblock_router.post("/", response_model=TextBlockResponse, status_code=status.HTTP_201_CREATED)
async def create_textblock(textblock_data: TextBlockCreate, service: TextblockService = Depends(get_textblock_service)):
    return await service.create_textblock(textblock_data)


@textblock_router.get("/{slug}", response_model=TextBlockResponse, status_code=status.HTTP_200_OK)
async def get_textblock_by_slug(slug: str, service: TextblockService = Depends(get_textblock_service)):
    textblock = await service.get_textblock_by_slug(slug)
    if textblock is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return textblock


@textblock_router.patch("/{textblock_id}", status_code=status.HTTP_200_OK)
async def update_textblock(textblock_id: str,
                           textblock_data: TextBlockUpdate,
                           service: TextblockService = Depends(get_textblock_service)):
    textblock = await service.update_textblock(textblock_id, textblock_data)
    if textblock is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return textblock


@textblock_router.delete("/{textblock_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_textblock(textblock_id: str,
                           service: TextblockService = Depends(get_textblock_service)):
    success = await service.delete_textblock(textblock_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ...

