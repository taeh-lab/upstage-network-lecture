from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from app.service.user_service import UserService

# create user
router = APIRouter(prefix="/users", tags=["users"])


class UserCreateRequest(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    created_at: str


@router.post("/", response_model=UserResponse)
async def create_user_api(
        user_create_request: UserCreateRequest,
):
    user_service = UserService()
    user_service.create_user(
        name=user_create_request.name,
        email=user_create_request.email
    )
    return UserResponse(
        id=0,
        name=user_create_request.name,
        email=user_create_request.email,
        created_at=str(datetime.now())
    )



@router.post("/", response_model=UserResponse)
async def create_user_api(
        user_create_request: UserCreateRequest,
):
    user_service = UserService()
    user_service.create_user(
        name=user_create_request.name,
        email=user_create_request.email
    )
    return UserResponse(
        id=0,
        name=user_create_request.name,
        email=user_create_request.email,
        created_at=str(datetime.now())
    )
