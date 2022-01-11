from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..core import oauth2, token
from ..db import database
from ..models import Model
from ..core import hashing, message, token
from ..schemas import UserSchema


router = APIRouter(
    prefix='/login',
    tags=['Authentication']
)


@router.post('/')
async def loginUser(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(Model.User).filter(
        Model.User.nip == request.username).first()
    if not user:
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Invalid Credentials!')
    if not hashing.Hash.verify(user.password, request.password):
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Invalid NIP/Password!')
    accessToken = token.create_access_token(data={"sub": user.nip})
    return {"access_token": accessToken, "token_type": "bearer"}


@router.get('/me', response_model=UserSchema.ShowUser)
async def getCurrentUser(current_user: UserSchema.User = Depends(oauth2.get_current_active_user), db: Session = Depends(database.get_db)):
    user = db.query(Model.User).filter(Model.User.nip == current_user).first()
    return user
