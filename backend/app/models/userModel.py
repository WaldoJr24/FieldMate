from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        # Damit MongoDB mit Pydantic-Modellen arbeiten kann
        orm_mode = True


