from datetime import datetime, timedelta
from typing import Optional
from pydantic.errors import DateTimeError
from jose import JWTError, jwt
from decouple import config
from ..schemas import LoginSchema

secretKey = config('SECRET_KEY')
algorithmConf = config('ALGORITHM')
accessTokenExpire = config('ACCESS_TOKEN_EXPIRE_MINUTES')


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = DateTimeError.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secretKey, algorithm=algorithmConf)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, secretKey, algorithms=[algorithmConf])
        nip: str = payload.get("sub")
        if nip is None:
            raise credentials_exception
        token_data = LoginSchema.TokenData(nip=nip)
    except JWTError:
        raise credentials_exception
    # user = getDb.query(Model.User).filter(Model.User.nip == nip).first()
    # if user is None:
    #     raise credentials_exception
    return token_data.nip
