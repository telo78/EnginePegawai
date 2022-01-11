from pydantic import BaseModel


class showProvider(BaseModel):
    name: str

    class Config():
        orm_mode = True


class Provider(BaseModel):
    name: str
    description: str

    class Config():
        orm_mode = True
