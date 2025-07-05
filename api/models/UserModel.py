from ...extensions import db
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(nullable=False)