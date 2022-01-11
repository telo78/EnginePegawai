from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    nip: str
    username: str
    email: str
    password: str
    status: int

    class Config():
        orm_mode = True


class CreateUser(BaseModel):
    nip: str
    username: str
    email: str
    password: str
    role: str


class UpdateUser(BaseModel):
    nip: Optional[str]
    username: Optional[str]
    email: Optional[str]
    status: Optional[str]


class ShowUser(BaseModel):
    id: int
    username: str
    nip: str
    email: str
    role: str
    status: int

    class Config():
        orm_mode = True
