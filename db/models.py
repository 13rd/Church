from sqlalchemy import Column, String, Boolean
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean(), default=True)
    hashed_password = Column(String, nullable=False)


class Images(Base):
    __tablename__ = "images"
    image_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_link = Column(String, nullable=False)


class News(Base):
    __tablename__ = "news"

    news_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_link = Column(String, nullable=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)

class Announcement(Base):
    __tablename__ = "announcements"
    announcement_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_link = Column(String, nullable=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)

class TextBlock(Base):
    __tablename__ = "textblock"

    textblock_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=True)
    body = Column(String, nullable=True, default="Text Sample")
