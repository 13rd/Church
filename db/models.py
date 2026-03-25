from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, UUID, func, Text, Index, Integer, ForeignKey
import uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

# Миксин для мягкого удаления
class SoftDeleteMixin:
    is_deleted: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True
    )


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    email: Mapped[str] = mapped_column(
        String(254),
        nullable=False,
        unique=True,
        index=True,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )
    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )


class News(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "news"

    news_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    # image_link: Mapped[str | None] = mapped_column(
    #     String(2048),
    #     nullable=True,
    # )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        index=True,
    )
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    # created_at: Mapped[datetime] = mapped_column(
    #     DateTime(timezone=True),
    #     nullable=False,
    #     server_default=func.now(),
    # )
    # updated_at: Mapped[datetime] = mapped_column(
    #     DateTime(timezone=True),
    #     nullable=True,
    #     onupdate=func.now(),
    #     default=func.now(),
    # )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    images: Mapped[list["NewsImage"]] = relationship(
        "NewsImage",
        back_populates="news",
        cascade="all, delete, delete-orphan",
        order_by="NewsImage.order_index",
        lazy="selectin"
    )


class NewsImage(Base):
    __tablename__ = "news_images"
    __table_args__ = ()

    image_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    news_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("news.news_id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    file_path: Mapped[str] = mapped_column(
        String(2048),
        nullable=False,
    )
    # public_url: Mapped[str] = mapped_column(
    #     String(2048),
    #     nullable=False,
    # )
    # order_index: Mapped[int] = mapped_column(
    #     Integer,
    #     default=0,
    #     nullable=False,
    # )
    # is_main: Mapped[bool] = mapped_column(
    #     Boolean,
    #     default=False,
    #     nullable=False,
    # )
    # alt_text: Mapped[str] = mapped_column(
    #     String(500),
    #     nullable=True,
    # )

    news: Mapped["News"] = relationship(
        "News",
        back_populates="images"
    )


class Announcement(Base):
    __tablename__ = "announcements"

    announcement_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        primary_key=True,
        default=uuid.uuid4,
    )
    image_link: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    body: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=func.now(),
        onupdate=func.now(),
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )


class TextBlock(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "textblock"

    textblock_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True,
    )
    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # __table_args__ = (
    #     Index("ix_text_blocks_slug_deleted", "slug", "deleted"),
    # )
