"""
FileName: REST Server
Author: N.G 4.9.22
Purpose: The REST server which takes user setup and event JSONs and uploads
         them to the elastic DB
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import datetime
from uuid import UUID
from ElasticHandler.ElasticHandler import ElasticHandler
import json


class Setup(BaseModel):
    """
    setup JSON for creating an old person's user
    """
    id: int
    name: str
    contacts: List[dict]
    Mail: Optional[str]
    phone: str


class Event(BaseModel):
    """
    event JSON for a specific event
    """
    EventID: int
    AgentID: str
    Sensor: str
    Message: str
    IsEmergency: bool
    strudel_timestamp: str


app = FastAPI()
data_pusher = ElasticHandler()


@app.get("/")
async def root():
    """
    classic GET test
    """
    return "penis"


def change_strudel_key(event_json):
    strudel_val = event_json["strudel_timestamp"]
    event_json.pop("strudel_timestamp", None)
    event_json["@timestamp"] = strudel_val
    return event_json


def push_data(index, post_data):
    json_data = json.loads(post_data.json())
    if index == "search-event":
        json_data = change_strudel_key(json_data)
        json_data["Timestamp"] = int(datetime.datetime.timestamp(datetime.datetime.now()))
    data_pusher.push_data(index, json_data)


@app.post("/setup")
async def create_setup(setup_account: Setup):
    """
    creates a setup account json from an agent (mocked) post
    :param setup_account
    """
    push_data("search-users", setup_account)


@app.post("/event")
async def create_event(event: Event):
    """
    creates an event json from an agent (mocked) post
    :param event
    """
    push_data("search-event", event)
