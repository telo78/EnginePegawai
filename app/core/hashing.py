from passlib.context import CryptContext
from decouple import config

salted = config('PASSWORD_SALT')

pwdCtx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
    def bcrypt(password: str):
        return pwdCtx.hash(password+salted)

    def verify(hashed_password, plain_password):
        plainPass = plain_password+salted
        return pwdCtx.verify(plainPass, hashed_password)
