from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from ..db import database
from ..schemas import CategorySchema, UserSchema
from ..controller import CategoryController
from ..core import oauth2

router = APIRouter(
    prefix='/category',
    tags=['Category']
)

getDb = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[CategorySchema.ShowCategory])
async def getAllCategory(db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CategoryController.getCategoryAll(db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=CategorySchema.ShowCategory)
async def getCategory(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CategoryController.getCategory(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def createCategory(request: CategorySchema.Category, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CategoryController.createCate(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def updateCategory(id: int, request: CategorySchema.Category, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CategoryController.updateCategory(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteCategory(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return CategoryController.deleteCategory(id, db)
