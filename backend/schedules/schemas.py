from pydantic import BaseModel, ConfigDict
from datetime import date


class Schedule(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    schedule_date: date
    image: str
