from dotenv import dotenv_values
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = dotenv_values(os.path.join(BASE_DIR, '.env'))

POSTGRES_USER=os.getenv("POSTGRES_USER",env["POSTGRES_USER"])
POSTGRES_PASSWORD=os.getenv("POSTGRES_PASSWORD",env["POSTGRES_PASSWORD"])
POSTGRES_DB=os.getenv("POSTGRES_DB",env["POSTGRES_DB"])
POSTGRES_HOST=os.getenv("POSTGRES_HOST", env["POSTGRES_HOST"])
DATABASE_URL=f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
ALEMBIC_URL=f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"