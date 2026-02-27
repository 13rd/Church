from datetime import datetime
from typing import List, Optional

from sqlalchemy import select

from db.models import TextBlock


class TextBlockDAL:

    def __init__(self, db_session):
        self.db_session = db_session

    async def create_textblock(self, textblock_data: dict) -> TextBlock:
        new_textblock = TextBlock(**textblock_data)
        self.db_session.add(new_textblock)
        return new_textblock

    async def get_all_textblocks(self, only_active: bool = True) -> List[TextBlock]:
        query = select(TextBlock)

        if not only_active:
            query = query.where(TextBlock.is_deleted == True)

        query = query.order_by(TextBlock.created_at.desc())

        results = await self.db_session.execute(query)
        return list(results.scalars().all())

    async def get_textblock_by_id(self, textblock_id: str, only_active: bool = True) -> Optional[TextBlock]:
        query = select(TextBlock).where(TextBlock.textblock_id == textblock_id)

        if not only_active:
            query = query.where(TextBlock.is_deleted == True)

        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def get_textblock_by_slug(self, textblock_slug: str, only_active: bool = True) -> Optional[TextBlock]:
        query = select(TextBlock).where(TextBlock.slug == textblock_slug)

        if not only_active:
            query = query.where(TextBlock.is_deleted == True)

        result = await self.db_session.execute(query)
        return result.scalar_one_or_none()

    async def update_textblock(self, textblock_id:str, textblock_data: dict) -> Optional[TextBlock]:
        textblock = await self.get_textblock_by_id(textblock_id)
        if not textblock:
            return None

        for key, value in textblock_data.items():
            if value is not None:
                setattr(textblock, key, value)

        textblock.updated_at = datetime.now()
        return textblock

    async def delete_textblock(self, textblock_id: str, is_soft: bool) -> bool:
        textblock = await self.get_textblock_by_id(textblock_id)
        if not textblock:
            return False

        if is_soft:
            textblock.is_deleted = True
        else:
            self.db_session.delete(textblock)

        textblock.updated_at = datetime.now()
        return True












