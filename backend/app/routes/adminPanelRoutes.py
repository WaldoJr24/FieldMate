from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.database import db
from app.models.userModel import User

#Hier die Routen für den Admin-Panel