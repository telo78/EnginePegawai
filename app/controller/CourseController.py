from fastapi import status
from sqlalchemy.orm.session import Session
from typing import List
from ..core import message
from ..models import Model
from ..schemas import CourseSchema, SaveCourseSchema
from sqlalchemy import or_, and_


def search(query: str, db: Session):
    courses = db.query(Model.Course).filter(or_(Model.Course.title.contains(query), Model.Course.instructors.contains(query))
                                            ).all()
    result = {"countAll": len(courses), "status": "success",
              "keyword": query,
              "data": courses}
    return result


def saveCourse(request: SaveCourseSchema, db: Session):
    checkDup = db.query(Model.SaveCourse).filter(and_(Model.SaveCourse.userId ==
                                                      request.userId, Model.SaveCourse.courseId == request.courseId)).first()
    if checkDup:
        message.sendMessage(status.HTTP_400_BAD_REQUEST, 'Already saved')
    savec = Model.SaveCourse(
        courseId=request.courseId,
        userId=request.userId
    )
    db.add(savec)
    db.commit()
    db.refresh(savec)
    return savec


def getSavedCourses(id: int, db: Session):
    savedcourses = db.query(Model.SaveCourse).filter(
        Model.SaveCourse.userId == id).all()
    # result = {"countAll": len(savedcourses), "status": "success",
    #           "data": List[savedcourses]}
    return savedcourses


def deleteSaveCourse(request: SaveCourseSchema, db: Session):
    checkDup = db.query(Model.SaveCourse).filter(and_(Model.SaveCourse.userId ==
                                                      request.userId, Model.SaveCourse.courseId == request.courseId))
    if not checkDup.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND,
                            'Saved course not found!')
    checkDup.delete(synchronize_session=False)
    db.commit()
    return {f'Saved course has been deleted '}


def create(request: CourseSchema, db: Session):
    newCourse = Model.Course(
        title=request.title,
        image=request.image,
        duration=request.duration,
        price=request.price,
        instructors=request.instructors,
        url=request.url,
        rating=request.rating,
        categoryId=request.categoryId,
        provider=request.provider
    )
    db.add(newCourse)
    db.commit()
    db.refresh(newCourse)
    return newCourse


def update(id: int, request: CourseSchema.Course, db: Session):
    course = db.query(Model.Course).filter(Model.Course.id == id)
    if not course.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Course not found!')
    course.update(request.dict(exclude_unset=True))
    db.commit()
    return {'Updated!'}


def getAll(db: Session, page: int, page_size: int, category: int, provider: int):
    if page_size > 100:
        page_size = 100
    # Base Query
    queryCourse = db.query(Model.Course)

    # Provider Present
    if provider:
        queryCourse = queryCourse.filter(
            Model.Course.providerId == provider)
    else:
        queryCourse
    # Category Present
    if category:
        queryCourse = queryCourse.filter(
            Model.Course.categoryId == category)
    else:
        queryCourse

    # Pagination
    if page and page_size:
        courses = queryCourse.limit(page_size).offset((page-1)*page_size).all()
    else:
        courses = queryCourse.limit(10).all()
    result = {"countAll": queryCourse.count(), "status": "success",
              "data": courses}

    return result


def get(id: int, db: Session):
    course = db.query(Model.Course).filter(Model.Course.id == id)
    if not course.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Course not found!')
    return course.first()


def delete(id: int, db: Session):
    course = db.query(Model.Course).filter(Model.Course.id == id)
    if not course.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Course not found!')
    course.delete(synchronize_session=False)
    db.commit()
    return {f'Course {id} has been deleted '}
