from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

# .env-Datei laden
load_dotenv()

# Verbindung aus Umgebungsvariable holen
MONGO_URL = os.getenv("MONGO_URL")

# MongoDB-Client erstellen
client = AsyncIOMotorClient(MONGO_URL)

# Datenbank benennen
db = client.fieldmate
