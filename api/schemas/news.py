import re
import uuid
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator


LETTER_MATCH_PATTERN = re.compile(r"^[а-яА-Яa-zA-Z\-]+$")


class TunedModel(BaseModel):
    class Config:
        orm_mode = True


class ShowNews(TunedModel):
    news_id: uuid.UUID
    image_name: str
    title: str
    body: str
    is_active: bool


class NewsCreate(BaseModel):
    image_name: str
    title: str
    body: str

    @field_validator("title")
    def validate_title(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422, detail="Title should contains only letters"
            )
        return value

    # @field_validator("surname")
    # def validate_surname(cls, value):
    #     if not LETTER_MATCH_PATTERN.match(value):
    #         raise HTTPException(
    #             status_code=422, detail="Surname should contains only letters"
    #         )
    #     return value
