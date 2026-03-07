import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from flask_login import UserMixin

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import db


class User(UserMixin, db.Model):
    __tablename__: str = "auth_user"

    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)
    username: Mapped[str] = mapped_column(sa.String(64), unique=True, nullable=False)
    password_hashed: Mapped[str] = mapped_column(sa.String(256), nullable=False)
    is_admin: Mapped[bool] = mapped_column(sa.Boolean(), nullable=False, server_default=sa.sql.false())

    def set_password(self, password: str):
        self.password_hashed = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hashed, password)
    
    def __repr__(self) -> str:
        return f"<User #{self.id} - {self.username}>"