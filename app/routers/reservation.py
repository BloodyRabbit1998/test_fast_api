from app.models.tables import Table, Reservation
from sqlalchemy import select,delete,func, and_, cast, String
from app.db.database import Session
from fastapi import APIRouter
from app.schemas.schemas_tables import *
from datetime import timedelta
from app.services.reservation import check_reservashin
router = APIRouter()

# gets

@router.get("/tables/",summary="список всех столиков")
async def get_tables() -> list|dict:
    try:
        async with Session() as session:
            stmt=select(Table).order_by(Table.name)
            rows=await session.scalars(stmt)
        rows=[TableSchema(
            id=row.id,
            name=row.name,
            seats=row.seats,
            location=row.location) 
            for row in rows]
        if rows:
            return rows
        else:
            return {"result":"No tables found"}
    except Exception as e:
        return {"result":"error","error":str(e)}
    

@router.get("/reservations/", summary="список всех броней")
async def get_reservations() -> list|dict:
    try:
        async with Session() as session:
            stmt=select(Reservation).order_by(Reservation.reservation_time)
            rows=await session.scalars(stmt)
        rows=[ReservationSchema(
                id=row.id,
                customer_name=row.customer_name,
                table_id=row.table_id,
                reservation_time=row.reservation_time,
                duration_minutes=row.duration_minutes)
                for row in rows]
        if rows:
            return rows
        else:
            return   {"result":"No reservations found"}
    except Exception as e:
        return {"result":"error","error":str(e)}
#posts
@router.post("/tables/", summary="добавить столик")
async def add_table(table: TableForm|list[TableForm]) -> dict:
    try:
        if type(table)==list:
            async with Session() as session:
                for t in table:
                    new_table=Table(**t.model_dump())
                    session.add(new_table)
                await session.commit()
            return {"result":"Tables added successfully"}
        else:
            async with Session() as session:
                new_table=Table(**table.model_dump())
                session.add(new_table)
                await session.commit()
            return {"result":"Table added successfully"}
    except Exception as e:
        return {"result":"error","error":str(e)}

@router.post("/reservations/", summary="добавить бронь")    
async def add_reservation(reservation: ReservationForm) -> dict:
    try:
        reservation.reservation_time.replace(tzinfo=None)  
        if await check_reservashin(reservation):
            return {"result":f"This time is already booked."}
        else:
            async with Session() as session:    
                new_reservation=Reservation(**reservation.model_dump())
                session.add(new_reservation)
                await session.commit()
            return {"result":"Reservation added successfully"}
    except Exception as e:
        return {"result":"error","error":str(e)}


#delete
@router.delete("/tables/{table_id}", summary="удалить столик")
async def delete_table(table_id: int) -> dict:
    try:
        async with Session() as session:
            stmt=delete(Table).where(Table.id==table_id)
            await session.execute(stmt)
            await session.commit()
        return {"result":"delete","id":table_id}
    except Exception as e:
        return {"result":"error","error":str(e)}
@router.delete("/reservations/{reservation_id}", summary="удалить бронь")
async def delete_reservation(reservation_id: int) -> dict:
    try:
        async with Session() as session:
            stmt=delete(Reservation).where(Reservation.id==reservation_id)
            await session.execute(stmt)
            await session.commit()
        return {"result":"delete","id":reservation_id}
    except Exception as e:
        return {"result":"error","error":str(e)}