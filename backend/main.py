import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles

from core.models import db_helper, Base
from schedules import schedule_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)    
    yield


app = FastAPI(lifespan=lifespan, version='0.1', title='ScheduleViewer')
app.include_router(schedule_router)
# Изменить папку со статикой!!!
app.mount('/schedules_images', StaticFiles(directory='schedules_images'), name='schedule_images')


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
