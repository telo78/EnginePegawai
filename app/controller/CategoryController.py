from fastapi import status
from sqlalchemy.orm.session import Session
from ..core import message
from ..models import Model
from ..schemas import CategorySchema


def createCate(request: CategorySchema.Category, db: Session):
    newCat = Model.Category(
        name=request.name,
        isActive=1
    )
    db.add(newCat)
    db.commit()
    db.refresh(newCat)

    return newCat


def getCategoryAll(db: Session):
    cats = db.query(Model.Category).all()
    return cats


def getCategory(id: int, db: Session):
    cat = db.query(Model.Category).filter(Model.Category.id == id)
    if not cat.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Category not found!')
    return cat.first()


def updateCategory(id: int, request: CategorySchema.Category, db: Session):
    cat = db.query(Model.Category).filter(Model.Category.id == id)
    if not cat.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Category not found!')
    cat.update(request.dict())
    db.commit()
    return {'Updated'}


def deleteCategory(id: int, db: Session):
    cat = db.query(Model.Category).filter(Model.Category.id == id)
    if not cat.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Category not found!')
    cat.delete(synchronize_session=False)
    db.commit()
    return {f'Category {id} has been deleted '}
