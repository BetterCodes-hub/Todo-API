from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, deps

router = APIRouter()

@router.post("/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(deps.get_db)):
    return crud.create_user(db, user)
