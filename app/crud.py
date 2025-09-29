from sqlalchemy.orm import Session
from . import models, schemas


def create_email(db: Session, email: schemas.EmailCreate): 
    priority_value = email.priority.value if hasattr(email.priority, "value") else email.priority
    db_email = models.EmailRecord(
        message_id=email.message_id,
        sender=email.sender,
        subject=email.subject,
        body=email.body,
        summary=email.summary,
        priority=priority_value
    )
    db.add(db_email)
    db.commit()
    db.refresh(db_email)
    return db_email

def get_emails(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.EmailRecord).order_by(models.EmailRecord.received_at.desc()).offset(skip).limit(limit).all()