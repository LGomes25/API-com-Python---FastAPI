import time

def sign_jwt(user_id: int) -> dict:
    now = time.time()
    payload = {
        "iss": "curso-fastapi.com.br",
        "sub": str(user_id),
        "aud": "curso-fastapi",
        "exp": now + (60 * 60 * 24),  # 24 horas
        "iat": now,
        "nbf": now,
    }
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token}
from fastapi import Request, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from typing import Optional

SECRET = "my-secret"
ALGORITHM = "HS256"

auth_scheme = HTTPBearer()

def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(auth_scheme)) -> dict:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM], audience="curso-fastapi")
        return payload
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
