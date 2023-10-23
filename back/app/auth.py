from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.config import JWT_EXPIRATION_TIME, JWT_SECRET_KEY


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm='HS256')
    
    return encoded_jwt

def decodeJWT(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Jetons expiré")
    except jwt.DecodeError:
        raise HTTPException(status_code=401, detail="Erreur de décodage du jeton")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Jeton invalide")

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwttoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = decodeJWT(jwttoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid