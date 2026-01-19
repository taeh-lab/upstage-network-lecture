from app.schemas.user import UserCreate, UserResponse
from datetime import datetime

class UserRepository:
    def __init__(self):
        self._users: dict[int, UserResponse] = {}
        self._current_id: int = 0

    def _next_id(self) -> int:
        self._current_id += 1
        return self._current_id

    def save_user(self, user_in: UserCreate) -> UserResponse:
        user_id = self._next_id()
        user = UserResponse(
            id=user_id,
            name=user_in.name,
            email=user_in.email,
            created_at=datetime.now().isoformat()
        )
        self._users[user_id] = user
        return user

# 애플리케이션 전체에서 단일 인스턴스로 사용될 user_repo 객체
user_repo = UserRepository()
