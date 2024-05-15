from datetime import date
from sqlalchemy import select
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from datetime import datetime

from core.models import Schedule
from core import settings


def get_current_date():
    return datetime.now().date()


async def upload_schedule(session: AsyncSession, image: UploadFile, schedule_date: date):
    with open(f'{settings.PATH_TO_IMAGES}/{schedule_date}.jpg', 'wb') as file:
        content = await image.read()
        file.write(content)
        file.close() 

    schedule = Schedule(
        schedule_date=schedule_date,
        image=schedule_date
    )

    try:
        session.add(schedule)
        await session.commit()
    except IntegrityError:
        pass
    # -
    return schedule


async def get_schedule(session: AsyncSession, schedule_date: date) -> Schedule | None:
    query = select(Schedule).where(Schedule.schedule_date == schedule_date)
    schedule = await session.execute(query)
    return schedule.scalar()
