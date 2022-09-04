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
    id: UUID
    name: str
    users: List[str]
    mail: Optional[str]
    phone_number: str


class Event(BaseModel):
    """
    event JSON for a specific event
    """
    event_id: UUID
    user_id: UUID
    event_type: int
    extra_info: Optional[Json[Any]]
    timestamp: datetime


app = FastAPI()


@app.get("/")
async def root():
    """
    classic GET test
    """
    return "penis"


@app.post("/setup")
async def create_setup(setup: Setup):
    """
    creates a setup json from an agent (mocked) post
    """
    index = "setup"
    json_setup = json.loads(setup.json())


@app.post("/event")
async def create_event(event: Event):
    """
    creates an event json from an agent (mocked) post
    """
    index = "event"
    json_event = json.loads(event.json())
