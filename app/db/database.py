from ..config import DATABASE_URL  
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine 

engine = create_async_engine(DATABASE_URL,echo=True)
Session = async_sessionmaker(engine)
