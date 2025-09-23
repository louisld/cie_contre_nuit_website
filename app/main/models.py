import datetime
import json
import pathlib
from typing import override

from flask import current_app
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
    short_description: Mapped[str] = mapped_column(sa.String(1000), nullable=True)
    active: Mapped[bool] = mapped_column(sa.Boolean(), nullable=False, default=False)

    is_future :Mapped[bool] = mapped_column(sa.Boolean(), nullable=False, default=True)
    start_date: Mapped[datetime.date] = mapped_column(sa.Date(), nullable=True)
    end_date: Mapped[datetime.date] = mapped_column(sa.Date(), nullable=True)

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


class Network:
    logo: str | None = None
    text: str | None = None

    def __init__(self, logo: str, text: str) -> None:
        self.logo = logo
        self.text = text


class Info:
    file_path= pathlib.Path(__file__).parent.parent / pathlib.Path("static/main/contact/uploads/info.json")

    def __init__(self, file_path: str | None=None) -> None:

        self.phone: str | None = None
        self.email: str | None = None
        self.networks: list[type[Network]] = []
        
        if file_path is not None:
            self.file_path = pathlib.Path(__file__).parent.parent / pathlib.Path(file_path)

        with open(self.file_path, 'r') as f:
            data = json.load(f)
            self.phone = data["phone"] if "phone" in data else None
            self.email = data["email"] if "email" in data else None

            if "networks" in data:
                for n in data["networks"]:
                    print(n)
                    try:
                        nt = Network(n["logo"], n["text"])
                        self.networks.append(nt)
                    except:
                        continue