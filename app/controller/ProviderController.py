from fastapi import HTTPException, status
from sqlalchemy.orm.session import Session
from ..core import message
from ..models import Model
from ..schemas import ProviderSchema


def create(request: ProviderSchema.Provider, db: Session):
    newProvider = Model.Provider(
        name=request.name,
        description=request.description
    )
    db.add(newProvider)
    db.commit()
    db.refresh(newProvider)
    return newProvider


def update(id: int, request: ProviderSchema.Provider, db: Session):
    provider = db.query(Model.Provider).filter(Model.Provider.id == id)
    if not provider.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Provider not found!')
    provider.update(request.dict(exclude_unset=True))
    db.commit()
    return {'Updated!'}


def delete(id: int, db: Session):
    provider = db.query(Model.Provider).filter(Model.Provider.id == id)
    if not provider.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Provider not found!')
    provider.delete(synchronize_session=False)
    db.commit()
    return {f'User {id} has been deleted '}


def get(id: int, db: Session):
    provider = db.query(Model.Provider).filter(Model.Provider.id == id)
    if not provider.first():
        message.sendMessage(status.HTTP_404_NOT_FOUND, 'Provider not found!')
    return provider.first()


def getAll(db: Session):
    providers = db.query(Model.Provider).all()
    return providers
