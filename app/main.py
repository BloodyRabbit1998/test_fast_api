from fastapi import FastAPI
from app.routers.reservation import router as reservation
import logging,uvicorn

"""TODO:
-tests
-fix add datetime reservation
"""

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(title="Restaurant Table Booking")
logger = logging.getLogger()


# Подключаем роутеры
app.include_router(reservation, tags=["Tables"])

if __name__ == '__main__':
    uvicorn.run(app='app.main:app', host="127.0.0.1", port=8000, reload=True)
    