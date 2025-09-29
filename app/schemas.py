from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum as PyEnum

class Priority(str , PyEnum):
    alta = "alta"
    media = "media"
    baja = "baja"

class EmailBase(BaseModel):
    message_id: Optional[str] = None
    sender: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None

class EmailCreate(EmailBase):
    summary: Optional[str] = None
    priority: Optional[Priority] = Priority.baja


class Email(EmailBase):
    id: int
    summary: Optional[str] = None
    priority: Priority
    notified: bool
    received_at: datetime

    class Config:
        orm_mode = True