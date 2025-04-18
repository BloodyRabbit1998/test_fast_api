from sqlalchemy import String,Integer,ForeignKey, DateTime
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            )

from app.db.base import Base

class Table(Base):
    """
Table – столик в ресторане:
    ○	id: int
    ○	name: str
    ○	seats: int (количество мест)
    ○	location: str 
"""
    __tablename__ = "Столики"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    name:Mapped[str] = mapped_column(String, unique=True)
    seats:Mapped[int] = mapped_column(Integer)
    location:Mapped[str] = mapped_column(String)
    def __str__(self):
        return f"{self.id} \t|\t{self.name}\t|\t{self.seats}\t|\t{self.location}"
class Reservation (Base):
    """
Reservation – бронь:
    ○	id: int
    ○	customer_name: str
    ○	table_id: int (FK на Table)
    ○	reservation_time: datetime
    ○	duration_minutes: int
    """
    __tablename__ = "Бронирование"
    id:Mapped[int] = mapped_column(primary_key=True, index=True)
    customer_name:Mapped[str] = mapped_column(String)
    table_id:Mapped[int] = mapped_column(ForeignKey(Table.id))
    reservation_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    duration_minutes: Mapped[int] = mapped_column(Integer)
    def __str__(self):
        return f"{self.id} \t|\t{self.customer_name}\t|\t{self.table_id}\t|\t{self.reservation_time}\t|\t{self.duration_minutes}"

