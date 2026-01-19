import logging
from fastapi import APIRouter
from datetime import datetime
from app.schemas.user import UserCreate, UserResponse

# 로거 인스턴스 가져오기
logger = logging.getLogger()

router = APIRouter()


@router.post("/", response_model=UserResponse, tags=["Users"])
def create_user(user: UserCreate):
    """
    Creates a user based on the input and returns the user's information
    with a hardcoded ID and a creation timestamp.
    """
    # 로그 기록 추가
    logger.info(f"Creating user: {user.name} with email: {user.email}")

    response = UserResponse(
        id=0,
        name=user.name,
        email=user.email,
        created_at=datetime.now().isoformat()
    )

    logger.info(f"User {user.name} created successfully with ID {response.id}")
    return response
