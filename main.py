"""
FileName: 
Author: N.G
Purpose:
"""

from fastapi import FastAPI
from pydantic import BaseModel, Json
from typing import Optional, List, Any
from datetime import datetime
from uuid import UUID
import json


class Setup(BaseModel):
    """
    setup JSON for creating an old person's user
    """
    ID: str
    name: str
    users: List[str]
    mail: Optional[str]
    phone_number: str


class Event(BaseModel):
    """
    event JSON for a specific event
    """
    event_ID: UUID
    user_ID: UUID
    event_type: int
    extra_info: Optional[Json[Any]]
    timestamp: datetime


app = FastAPI()


@app.get("/")
async def root():
    return "penis"


@app.post("/setup")
async def create_setup(setup: Setup):
    json_setup = json.loads(setup.json())
    json_setup["index"] = "setup"


@app.post("/event")
async def create_event(event: Event):
    json_event = json.loads(event.json())
    json_event["index"] = "event"
