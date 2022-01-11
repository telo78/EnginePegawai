from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from ..core import token as tk
from ..schemas import UserSchema

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return tk.verify_token(token, credentials_exception)


async def get_current_active_user(current_user: UserSchema.User = Depends(get_current_user)):
    return current_user
