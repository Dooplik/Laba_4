from typing import Dict
from pydantic import BaseModel
from datetime import datetime


class GetInfo(BaseModel):
    created_at: str
    updated_at: str


class GetText(BaseModel):
    id: int
    text: str


class Create(BaseModel):
    id: int


class Delete(BaseModel):
    removed_id: int


class Update(BaseModel):
    id: int
    text: str


class GetList(BaseModel):
    notes_list: Dict[int, int]
