"""
FileName: 
Author: N.G
Purpose:
"""

from fastapi import FastAPI
from pydantic import BaseModel, Json
from typing import Union, List, Any
from datetime import datetime
from uuid import UUID


class Setup(BaseModel):
    """
    setup JSON for creating an old person's user
    """
    ID: UUID
    name: str
    users: List[str]
    mail: Union[str, None] = None
    phone_number: str


class Event(BaseModel):
    """
    event JSON for a specific event
    """
    event_ID: UUID
    user_ID: UUID
    event_type: int
    extra_info: Union[Json[Any], None] = None
    timestamp: datetime


app = FastAPI()


@app.get("/")
async def root():
    return "penis"





