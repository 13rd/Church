import re
import uuid
from datetime import datetime
from typing import Optional
import bleach
from pydantic import BaseModel, field_validator, ConfigDict, Field

TITLE_PATTERN = re.compile(r"^[\w\s\-\,\.\!\?\:\'\"А-Яа-я]+$")

class NewsBase(BaseModel):
    title: str = Field(..., min_length=5, max_length=200, description="News title")
    body: str = Field(..., min_length=5, description="News body")
    image_link: Optional[str] = Field(default=None, description="News image link")
    is_active: bool = Field(default=True, description="News active")

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: str) -> str:
        if not TITLE_PATTERN.match(value):
            raise ValueError("Invalid title")
        return value

    @field_validator("body")
    @classmethod
    def sanitize_body(cls, value: str) -> str:
        allowed_tags = ["p", "br", "strong", "em", "u", "h1", "h2", "h3", "ul", "ol", "li", "a"]
        return bleach.clean(value, tags=set(allowed_tags), strip=True)

    @field_validator("image_link")
    @classmethod
    def validate_image_link(cls, value: str) -> str:
        if value is not None or value != "":
            if not value.startswith(("http://", "https://")):
                raise ValueError("Invalid image link")
        return value


class NewsResponse(NewsBase):
    model_config = ConfigDict(from_attributes=True)

    news_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    ...


class NewsUpdate(BaseModel):
    """Схема для обновления (все поля опциональные)"""
    title: Optional[str] = Field(None, min_length=5, max_length=200)
    body: Optional[str] = Field(None, min_length=10)
    image_link: Optional[str] = Field(None)
    is_active: Optional[bool] = Field(None)

    @field_validator("title")
    @classmethod
    def validate_title(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not TITLE_PATTERN.match(value):
            raise ValueError("Invalid title characters")
        return value

    @field_validator("image_link")
    @classmethod
    def validate_image_link(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and not value.startswith(("http://", "https://")):
            raise ValueError("Invalid image link protocol")
        return value

    @field_validator("body")
    @classmethod
    def sanitize_body(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            allowed_tags = ["p", "br", "strong", "em", "u", "h1", "h2", "h3", "ul", "ol", "li", "a"]
            return bleach.clean(value, tags=set(allowed_tags), strip=True)
        return value
