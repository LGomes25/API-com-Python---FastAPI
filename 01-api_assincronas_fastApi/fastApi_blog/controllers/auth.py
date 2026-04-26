
from fastapi import APIRouter
from fastApi_blog.schemas.auth import LoginIn
from fastApi_blog.views.auth import LoginOut
from fastApi_blog.security import sign_jwt

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)
