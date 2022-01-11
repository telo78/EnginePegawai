from typing import List, Optional
from pydantic import BaseModel
from .ProviderSchema import showProvider
from .CategorySchema import Category


class Course(BaseModel):
    id: int
    title: str
    image: str
    duration: Optional[int]
    price: Optional[str]
    instructors: str
    url: str
    rating: Optional[float]
    providers: showProvider
    category: Category

    class Config():
        orm_mode = True


class showSCourses(BaseModel):
    id: int
    title: str
    image: str
    url: str
    providers: showProvider
    category: Category

    class Config():
        orm_mode = True


class showCourse(BaseModel):
    countAll: int
    status: str
    data: List[Course]

    class Config():
        orm_mode = True
