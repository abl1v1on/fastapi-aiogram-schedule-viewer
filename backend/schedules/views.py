from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import date

from . import utils
from core import settings
from .schemas import Schedule
from core.models import db_helper


router = APIRouter(
    prefix='/schedules',
    tags=['Schedule']
)

SessionDependency = Depends(db_helper.session_dependency)


@router.get('', response_model=Schedule)
async def get_today_schedule(session: AsyncSession = SessionDependency, schedule_date: date = utils.get_current_date()):
    schedule = await utils.get_schedule(session, schedule_date)

    if schedule:
        return FileResponse(
            path=f'{settings.PATH_TO_IMAGES}/{schedule_date}.jpg',
            status_code=status.HTTP_200_OK,
            filename=f'{schedule_date}.jpg',
            media_type='multipart/form-data'
        )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Расписание за {schedule_date} не найдено'
    )


@router.post('')
async def upload_schedule(image: UploadFile, schedule_date: date = utils.get_current_date(), session: AsyncSession = SessionDependency):
    return await utils.upload_schedule(session, image, schedule_date)
