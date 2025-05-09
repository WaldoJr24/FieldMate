from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str
    password: str = Field(..., min_length=8)
    role: str = Field(default="technician", description="User role")

    class Config:
        schema_extra = {
            "example": {
                "username": "maxmustermann",
                "email": "max@example.com",
                "password": "supersecret123",
                "role": "technician"
            }
        }

# UserLogin Schema (siehe oben)
class UserLogin(BaseModel):
    usernameOrEmail: str = Field(..., alias="username_or_email")
    password: str
