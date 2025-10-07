from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from sqlalchemy import Enum as SQLEnum
from .database import Base
import enum 


class PriorityEnum(str, enum.Enum):
    alta= "alta"
    media="media"
    baja="baja"

class EmailRecord(Base):
    __tablename__ = "emails"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, unique=True, index=True, nullable=True)
    sender = Column(String, index=True, nullable=True)
    subject = Column(String, nullable=True)
    body = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)
    priority = Column(SQLEnum(PriorityEnum), default=PriorityEnum.baja)
    notified = Column(Boolean, default=False)
    received_at = Column(DateTime, default=func.now())