from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api.models import UserCreate, ShowUser
from db.dals import UserDAL
from db.session import get_db
from typing import List


user_router = APIRouter()


async def _create_new_user(body: UserCreate, db) -> ShowUser:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            user = await user_dal.create_user(
                name=body.name,
                surname=body.surname,
                email=body.email,
            )
        return ShowUser(
            user_id=user.user_id,
            name=user.name,
            surname=user.surname,
            email=user.email,
            is_active=user.is_active,
        )


async def _get_all_users(db) -> List[ShowUser]:
    async with db as session:
        async with session.begin():
            user_dal = UserDAL(session)
            result = list(await user_dal.get_all_users())
            return result


@user_router.post("/", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)


@user_router.get("/", response_model=List[ShowUser])
async def get_users(db: AsyncSession = Depends(get_db)) -> List[ShowUser]:
    return await _get_all_users(db)
