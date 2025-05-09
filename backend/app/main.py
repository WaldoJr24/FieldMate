from fastapi import FastAPI
from app.routes import userRoutes
from app.routes import orderRoutes  # Auth-Route importieren

app = FastAPI()

# User-Route einfügen
app.include_router(userRoutes.router, prefix="/api/user", tags=["User"])
# Auth-Route einfügen
app.include_router(orderRoutes.protectedRouter, prefix="/api/orders", tags=["Order"])

@app.get("/")
async def root():
    return {"message": "Welcome to FieldMate API 🚀"}
