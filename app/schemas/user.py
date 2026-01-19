from pydantic import BaseModel, Field
from datetime import datetime


class UserCreate(BaseModel):
    name: str = Field(..., description="User's name", example="John Doe")
    email: str = Field(..., description="User's email address", example="john.doe@example.com")


class UserResponse(BaseModel):
    id: int = Field(..., description="Unique identifier for the user", example=0)
    name: str = Field(..., description="User's name", example="John Doe")
    email: str = Field(..., description="User's email address", example="john.doe@example.com")
    created_at: str = Field(..., description="Timestamp of user creation", example=datetime.now().isoformat())
