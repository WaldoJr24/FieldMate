from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    username: str
    email: str
    password: str
    role: Literal["planner", "technician"] = "technician"  # Standardwert ist "technician"

    class Config:
        # Damit MongoDB mit Pydantic-Modellen arbeiten kann
        orm_mode = True


