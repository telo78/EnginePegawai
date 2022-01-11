from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm.session import Session
from ..db import database
from ..schemas import UserSchema, ProviderSchema
from ..core import oauth2
from ..controller import ProviderController


router = APIRouter(
    prefix="/provider",
    tags=["Provider"]
)

getDb = database.get_db


@router.get('/', status_code=status.HTTP_200_OK)
async def getAllProvider(db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return ProviderController.getAll(db)


@router.get('/{id}', status_code=status.HTTP_200_OK)
async def getProvider(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return ProviderController.get(id, db)


@router.post('/', status_code=status.HTTP_201_CREATED)
async def createProvider(request: ProviderSchema.Provider, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return ProviderController.create(request, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
async def updateProvider(id: int, request: ProviderSchema.Provider, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return ProviderController.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteProvider(id: int, db: Session = Depends(getDb), current_user: UserSchema.User = Depends(oauth2.get_current_user)):
    return ProviderController.delete(id, db)
