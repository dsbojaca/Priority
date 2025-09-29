from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal, Base

# crear tablas (si no existen)
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Priority API")

# dependencia para obtener sesión DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def read_root():
    return{'message': 'Welcome to the Priority API'}


@app.post("/emails/", response_model=schemas.Email)
def create_email(email: schemas.EmailCreate, db: Session = Depends(get_db)):
    # evita duplicados por message_id
    if email.message_id:
        existing = db.query(models.EmailRecord).filter(models.EmailRecord.message_id == email.message_id).first()
        if existing:
            raise HTTPException(status_code=400, detail="Email with this message_id already exists")
    return crud.create_email(db, email)

@app.get("/emails/", response_model=list[schemas.Email])
def list_emails(skip: int= 0, limit: int=100, db: Session = Depends(get_db)):
    return crud.get_emails(db, skip=skip, limit=limit)