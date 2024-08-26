from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.infraestructure.database_settings import get_database_setting

DATABASE_URL = get_database_setting().database_connection
ASYNC_DATABASE_URL = get_database_setting().async_database_connection

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
async_engine = create_async_engine(
    ASYNC_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = sessionmaker(
    bind=async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False)

Base = declarative_base()


async def get_async_db():
    async with AsyncSessionLocal() as session:
        yield session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
