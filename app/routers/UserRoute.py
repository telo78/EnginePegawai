from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from ..db import database
from ..schemas import UserSchema
from ..controller import UserController
from ..core import oauth2


router = APIRouter(
    prefix='/user',
    tags=['User']
)

getDb = database.get_db


@router.get('/{id}',  response_model=UserSchema.ShowUser, status_code=status.HTTP_200_OK)
async def getUser(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return UserController.show(id, db)


@router.get('/',  response_model=List[UserSchema.ShowUser], status_code=status.HTTP_200_OK)
async def getAllUser(db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return UserController.showAll(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def createUser(request: UserSchema.CreateUser, db: Session = Depends(getDb)):
    return UserController.createUser(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def updateUser(id: int, request: UserSchema.UpdateUser,  db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return UserController.updateData(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return UserController.deleteData(id, db)
