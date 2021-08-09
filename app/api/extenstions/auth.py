import time
from app.schemas.user import UserInJWT
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from configs.jwt import ALGORITHM, JWT_KEY


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code=403, detail='Неверная схема аутентификации. Используется Bearer.')
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail='Неверный токен или время жизни токена изтекло.')
            return self.decode_jwt(credentials.credentials)
        else:
            raise HTTPException(status_code=403, detail='Неверный код авторизации.')

    def decode_jwt(self, token: str) -> UserInJWT:
        decoded_token = jwt.decode(token, JWT_KEY, algorithms=[ALGORITHM])
        return UserInJWT(**decoded_token) if decoded_token['exp'] >= time.time() else None

    def verify_jwt(self, token: str) -> bool:
        is_token_valid: bool = False
        try:
            payload = self.decode_jwt(token)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return is_token_valid


class PermissionDenied(Exception):
    pass
