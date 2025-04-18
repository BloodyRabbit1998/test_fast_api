from app.models.tables import Table, Reservation
from app.schemas.schemas_tables import ReservationForm
from sqlalchemy import select
from app.db.database import Session
from datetime import timedelta,datetime
async def check_reservashin(reservation: ReservationForm):
    async with Session() as session:
        stmt = select(Reservation).where(
                    Reservation.table_id==reservation.table_id,
                )
        print('\n'*5)
        rows = await session.scalars(stmt)
        for row in rows:
            print(rows)
            start,end=row.reservation_time,row.reservation_time+timedelta(minutes=row.duration_minutes)
            if start<=reservation.reservation_time<=end:
                return True
        return False