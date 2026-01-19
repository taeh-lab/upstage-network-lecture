import re
from datetime import datetime
from app.schemas.user import UserCreate, UserResponse

class UserService:
    def _is_valid_email(self, email: str) -> bool:
        """
        Validates the email format using a more robust regular expression.
        """
        # A more common and robust regex for email validation
        pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(pattern, email) is not None

    def create_user(self, user_in: UserCreate) -> UserResponse:
        """
        Validates email and creates a user response object.
        """
        if not self._is_valid_email(user_in.email):
            raise ValueError("Invalid email format")

        # Business logic for creating a user
        # (currently returns a mock response)
        return UserResponse(
            id=0,
            name=user_in.name,
            email=user_in.email,
            created_at=datetime.now().isoformat()
        )
