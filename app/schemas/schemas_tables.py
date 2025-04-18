from pydantic import BaseModel,Field
from datetime import datetime

class TableSchema(BaseModel):
    id: int
    name: str
    seats: int =Field(gt=0,lt=100)
    location: str 
class ReservationSchema(BaseModel):
    id: int
    customer_name: str
    table_id: int
    reservation_time:   datetime
    duration_minutes: int =Field(gt=0)

class TableForm(BaseModel):
    name: str
    seats: int =Field(gt=0,lt=100)
    location: str
class ReservationForm(BaseModel):
    customer_name: str
    table_id: int
    reservation_time:   datetime
    duration_minutes: int =Field(gt=0)
