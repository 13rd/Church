from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class TextBlockBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=100, description="Название текстового блока")
    body: str = Field(..., min_length=5, description="Текст на сайте")
    slug: str = Field(..., pattern=r"^[-a-zA-Z0-9_]+$", description="Уникальное название")

class TextBlockCreate(TextBlockBase):
    ...

class TextBlockUpdate(TextBlockBase):
    title: Optional[str] = Field(None, min_length=5, max_length=255)
    body: Optional[str] = Field(None, min_length=5)


class TextBlockResponse(TextBlockBase):
    textblock_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

