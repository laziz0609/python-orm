from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)
from sqlalchemy import String, Boolean, ForeignKey

from .base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(128), nullable=False)
    last_name: Mapped[str] = mapped_column(String(128))
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")

    def __str__(self):
        return f'User(user_id={self.user_id}, username="{self.username}", first_name="{self.first_name}", last_name="{self.last_name}, profile={self.profile}")'

    def __repr__(self):
        return f'User(user_id={self.user_id}, username="{self.username}", first_name="{self.first_name}", last_name="{self.last_name}, profile={self.profile}")'


class Profile(Base):
    __tablename__ = "profile"

    profile_id: Mapped[int] = mapped_column(primary_key=True)
    bio: Mapped[str] = mapped_column(String(512))
    picture_url: Mapped[str] = mapped_column(String(512))
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE"), unique=True
    )

    user: Mapped["User"] = relationship(back_populates="profile")

    def __str__(self):
        return f'Profile(profile_id={self.profile_id}, bio="{self.bio}", picture_url="{self.picture_url}")'

    def __repr__(self):
        return f'Profile(profile_id={self.profile_id}, bio="{self.bio}", picture_url="{self.picture_url}")'


class Post(Base):
    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(512))
    content: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE")
    )

    user: Mapped["User"] = relationship(back_populates="posts")

    def __str__(self):
        return f'Post(post_id={self.post_id}, title="{self.title}", content="{self.content}")'

    def __repr__(self):
        return f'Post(post_id={self.post_id}, title="{self.title}", content="{self.content}")'
