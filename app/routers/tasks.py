from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, deps

router = APIRouter()

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    return crud.create_task(db, task, current_user.id)

@router.get("/", response_model=list[schemas.Task])
def read_tasks(db: Session = Depends(deps.get_db), current_user=Depends(deps.get_current_user)):
    return crud.get_tasks(db, current_user.id)