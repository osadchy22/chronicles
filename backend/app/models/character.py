from datetime import datetime, timezone

from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Character(Base):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    level: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    experience: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=0,
    )

    gold: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=100,
    )

    reserved_gold: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        default=0,
    )

    energy: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=100,
    )

    max_energy: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=100,
    )

    hp: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=100,
    )

    max_hp: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=100,
    )

    strength: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    vitality: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    agility: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    intelligence: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    luck: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=5,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    user = relationship(
        "User",
        back_populates="character",
    )

    @property
    def available_gold(self) -> int:
        return self.gold - self.reserved_gold