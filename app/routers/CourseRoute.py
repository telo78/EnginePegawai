from typing import List, Optional
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..db import database
from ..schemas import CourseSchema, UserSchema, SaveCourseSchema
from ..core import oauth2
from ..controller import CourseController


router = APIRouter(
    prefix="/course",
    tags=["Course"]
)

getDb = database.get_db


@router.get('/', response_model=CourseSchema.showCourse, status_code=status.HTTP_200_OK)
async def getAllCourse(db: Session = Depends(getDb), page: Optional[int] = 0, page_size: Optional[int] = 0, category: Optional[int] = None, provider: Optional[int] = None):
    return CourseController.getAll(db, page, page_size, category, provider)


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def getCourse(id: int, db: Session = Depends(getDb)):
    return CourseController.get(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def createCourse(request: CourseSchema.Course, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CourseController.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def updateCourse(id: int, request: CourseSchema.Course, db: Session = Depends(getDb),  current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CourseController.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteCourse(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CourseController.delete(id, db)


@router.get('/search/', status_code=status.HTTP_202_ACCEPTED)
async def searchCourse(query: Optional[str], db: Session = Depends(getDb)):
    return CourseController.search(query, db)


@router.post('/savecourse/insert/', response_model=SaveCourseSchema.SaveCourse, status_code=status.HTTP_201_CREATED)
async def saveCourses(request: SaveCourseSchema.SaveCourse, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CourseController.saveCourse(request, db)


@router.post("/savecourse/delete/", status_code=status.HTTP_202_ACCEPTED)
async def deleteSaveCourses(request: SaveCourseSchema.SaveCourse, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CourseController.deleteSaveCourse(request, db)


@router.get("/savecourse/{id}", response_model=List[SaveCourseSchema.showSavedCourse], status_code=status.HTTP_200_OK)
async def getSavedCourses(id: int, db: Session = Depends(getDb)):
    return CourseController.getSavedCourses(id, db)
