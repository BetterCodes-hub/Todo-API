from pydantic import BaseModel, EmailStr
from typing import List, Optional

class TaskBase(BaseModel):
    title: str
    description: Optional[str]= None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    tasks: List[Task] = []
    
    class Config:
        orm_mode = True
