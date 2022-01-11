from datetime import datetime
from pydantic import BaseModel


class Category(BaseModel):
    name: str

    class Config():
        orm_mode = True


class ShowCategory(BaseModel):
    id: int
    isActive: int
    name: str
    createdAt: datetime

    class Config():
        orm_mode = True
