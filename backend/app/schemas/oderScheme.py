from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrderCreate(BaseModel):
    orderid: str
    customername: str
    creationdate: datetime
    executiondate: datetime
    machinetype: str

    class config:
        schema_extra = { 
            "example": {
                "orderid": "12345",
                "customername": "Musterfirma",
                "creationdate": "2023-10-01T12:00:00Z",
                "executiondate": "2023-10-10T12:00:00Z",
                "machinetype": "CNC-Maschine"
            }
        }

class OrderUpdate(BaseModel):
    status: str