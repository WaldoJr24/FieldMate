from fastapi import APIRouter, HTTPException
from app.models.userModel import User
from app.schemas.userScheme import UserCreate, UserLogin
from app.database import db
from app.auth import create_access_token, get_current_user
from passlib.context import CryptContext


# TODO: Register nur für Admins erlauben (in admin panel) -> nur admin kann user anlegen
#       Bei login: role abfragen (user/planner/admin) -> dann den richtigen token zurückgeben -> Technician sieht nur Startseite mit Aufträge
#                                                                                                Planner zusätzlich das Fragment auftragerstellen
#                                                                                                Admin sieht alles also zusätzlich noch sein panel                                           



router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    # Überprüfen, ob der Benutzer bereits existiert
    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Passwort hashen
    hashed_password = pwd_context.hash(user.password)

    # Neuen Benutzer in der DB speichern
    new_user = {**user.dict(), "password": hashed_password}  # Passwort ersetzen
    result = await db["users"].insert_one(new_user)

    # Benutzer aus der DB zurückholen
    created_user = await db["users"].find_one({"_id": result.inserted_id})

    return User(**created_user)



# Login Route
@router.post("/login")
async def login(user: UserLogin):
    # Suche nach dem Benutzer in der Datenbank
    existing_user = await db["users"].find_one(
        {"$or": [{"username": user.usernameOrEmail}, {"email": user.usernameOrEmail}]}
    )
    
    # Wenn der Benutzer nicht existiert, gebe einen Fehler zurück
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Prüfen, ob das Passwort korrekt ist (Passwort-Hashing)
    if not pwd_context.verify(user.password, existing_user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    # Wenn alles erfolgreich ist, Token erstellen
    access_token = create_access_token(
        data={"sub": existing_user["username"]}  # Das "sub" im Token ist der Benutzername
    )
    return {"access_token": access_token, "token_type": "bearer"}
    

