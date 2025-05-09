from pydantic import BaseModel
from datetime import datetime

class Order(BaseModel):
    orderid: str
    customername: str
    creationdate: datetime
    executiondate: datetime
    machinetype: str
    status: str
    
    class Config:
        # Damit MongoDB mit Pydantic-Modellen arbeiten kann
        orm_mode = True


