from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from api.schemas.textblock import TextBlockCreate, TextBlockUpdate, TextBlockResponse
from db.dals.textblock import TextBlockDAL


class TextblockService:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session
        self.dal = TextBlockDAL(db_session)

    async def create_textblock(self, textblock_data: TextBlockCreate) -> TextBlockResponse:
        textblock = await self.dal.create_textblock(textblock_data.model_dump())
        await self.db_session.commit()
        await self.db_session.refresh(textblock)

        return TextBlockResponse.model_validate(textblock)


    async def get_all_textblocks(self) -> List[TextBlockResponse]:
        textblocks = await self.dal.get_all_textblocks()
        return [TextBlockResponse.model_validate(textblock) for textblock in textblocks]


    async def get_textblock_by_id(self, textblock_id: str) -> Optional[TextBlockResponse]:
        textblock = await self.dal.get_textblock_by_id(textblock_id)
        if not textblock:
            return None
        return TextBlockResponse.model_validate(textblock)


    async def get_textblock_by_slug(self, textblock_slug: str) -> Optional[TextBlockResponse]:
        textblock = await self.dal.get_textblock_by_slug(textblock_slug)
        if not textblock:
            return None
        return TextBlockResponse.model_validate(textblock)


    async def update_textblock(self, textblock_id: str, textblock_data: TextBlockUpdate) -> Optional[TextBlockResponse]:
        updated_textblock = textblock_data.model_dump()
        textblock = await self.dal.update_textblock(textblock_id, updated_textblock)

        if not textblock:
            return None

        await self.db_session.commit()
        await self.db_session.refresh(textblock)
        return TextBlockResponse.model_validate(textblock)


    async def delete_textblock(self, textblock_id: str) -> bool:
        result = await self.dal.delete_textblock(textblock_id)

        if result:
            await self.db_session.commit()
        return result




