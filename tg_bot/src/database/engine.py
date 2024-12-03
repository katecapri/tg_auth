import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

engine = create_async_engine(f'postgresql+asyncpg://{os.getenv("DB_USERNAME")}:{os.getenv("DB_PASSWORD")}'
                             f'@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_DATABASE")}', echo=False,
                             poolclass=NullPool)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
