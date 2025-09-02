from typing import override
import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.extensions import db

class Project(db.Model):
    __tablename__: str = "main_project"

    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    short_title: Mapped[str] = mapped_column(sa.String(64), nullable=False, unique=True)
    short_description: Mapped[str] = mapped_column(sa.String(255), nullable=True)
    active: Mapped[bool] = mapped_column(sa.Boolean(), nullable=False, default=False)

    @override
    def __repr__(self) -> str:
        return f"<Project #{self.id} - {self.short_title}>"

class Member(db.Model):
    __tablename__:str = "main_member"

    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    first_name: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String(64), nullable=False)
    role: Mapped[str] = mapped_column(sa.String(64), nullable=False, default="Membre")

    @override
    def __repr__(self) -> str:
        return f"<Member #{self.id} - {self.first_name} {self.last_name}>"