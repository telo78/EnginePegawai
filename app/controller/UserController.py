from fastapi import status
from sqlalchemy.orm.session import Session
from ..core import message, hashing
from ..models import Model
from ..schemas import UserSchema


def createUser(request: UserSchema.CreateUser, db: Session):
    newUser = Model.User(
        email=request.email,
        nip=request.nip,
        role="Admin",
        username=request.username,
        password=hashing.Hash.bcrypt(request.password),
        status=1
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser


def show(id: int, db: Session):
    users = db.query(Model.User).filter(Model.User.id == id)
    if not users.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'User not found!')
    return users.first()


def showAll(db: Session):
    users = db.query(Model.User).all()
    return users


def updateData(id: int, request: UserSchema.UpdateUser, db: Session):
    users = db.query(Model.User).filter(Model.User.id == id)
    if not users.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'User not found!')
    users.update(request.dict(exclude_unset=True))
    db.commit()
    return {'Updated'}


def deleteData(id: int, db: Session):
    user = db.query(Model.User).filter(Model.User.id == id)
    if not user.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'User not found!')
    user.delete(synchronize_session=False)
    db.commit()
    return {f'User {id} has been deleted '}
