"""
FileName: REST Server
Author: N.G 4.9.22
Purpose: The REST server which takes user setup and event JSONs and uploads
         them to the elastic DB
"""

from fastapi import FastAPI
from pydantic import BaseModel, Json
from typing import Optional, List, Any
from datetime import datetime
from uuid import UUID
from ElasticHandler.ElasticHandler import ElasticHandler
import json


class Setup(BaseModel):
    """
    setup JSON for creating an old person's user
    """
    id: UUID
    name: str
    contacts: List[dict]
    mail: Optional[str]
    phone: str


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
data_pusher = ElasticHandler()


@app.get("/")
async def root():
    """
    classic GET test
    """
    return "penis"


@app.post("/setup")
async def create_setup(setup_account: Setup):
    """
    creates a setup account json from an agent (mocked) post
    :param setup_account
    """
    index = "search-users"
    json_setup_account = json.loads(setup_account.json())
    data_pusher.push_data(index, json_setup_account)


@app.post("/event")
async def create_event(event: Event):
    """
    creates an event json from an agent (mocked) post
    :param event
    """
    index = "search-event"
    json_event_account = json.loads(event.json())
    data_pusher.push_data(index, json_event_account)
