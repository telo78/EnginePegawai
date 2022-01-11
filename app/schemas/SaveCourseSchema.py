from typing import List
from pydantic import BaseModel
from .UserSchema import ShowUser
from .CourseSchema import showSCourses


class SaveCourse(BaseModel):
    courseId: int
    userId: int

    class Config():
        orm_mode = True


class showSavedCourse(BaseModel):
    courses: showSCourses

    class Config():
        orm_mode = True
