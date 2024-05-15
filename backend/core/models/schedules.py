from sqlalchemy.orm import Mapped, mapped_column
from datetime import date

from . import Base


class Schedule(Base):
    __tablename__ = 'schedules'

    id: Mapped[int] = mapped_column(primary_key=True)
    schedule_date: Mapped[date] = mapped_column(unique=True)
    image: Mapped[str]
