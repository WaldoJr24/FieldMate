from fastapi import APIRouter, Depends
from app.auth import get_current_user
from app.database import db
from app.models.orderModel import Order
from app.schemas.oderScheme import OrderCreate, OrderUpdate
from app.auth import get_current_user


# TODO: createOrder nur für Planner und Admin erlauben,
#       JWT Token abfragen



protectedRouter = APIRouter()

# Eine Route, die nur für authentifizierte Benutzer zugänglich ist
@protectedRouter.get("/getAllOrders")
async def get_all_orders(current_user: str = Depends(get_current_user)):
    # Alle Bestellungen aus der Datenbank abrufen
    orders = await db["orders"].find().to_list(length=100)
    return {"message": f"Hello, {current_user}, you have access to all orders!", "orders": orders}


@protectedRouter.get("/getOrder/{order_id}")
async def get_order(order_id: str, current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}, you have access to order {order_id}!"}


@protectedRouter.post("/createOrder", response_model=Order)
async def create_order(order: OrderCreate): #dass muss nachher hinter OrderCreater zum prüfen des JWT tokens   , current_user: str = Depends(get_current_user)   PRÜFEN AUF PLANNER!
    if not order:
        return {"message": "Order data is required!"}
    # Order in der Datenbank speichern
    result = await db["orders"].insert_one(order.dict())
    created_order = await db["orders"].find_one({"_id": result.inserted_id})
    return {"message": f"Order {created_order['orderid']} created successfully!"}

@protectedRouter.put("/updateOrder/{order_id}", response_model=Order)
async def update_order(order_id: str, order: OrderUpdate, current_user: str = Depends(get_current_user)):
    # Order in der Datenbank aktualisieren
    result = await db["orders"].update_one({"_id": order_id}, {"$set": order.dict()})
    if result.modified_count == 0:
        return {"message": "Order not found or no changes made!"}
    updated_order = await db["orders"].find_one({"_id": order_id})
    return {"message": f"Order {updated_order['orderid']} updated successfully!"}
    

