from uuid import uuid4
from sqlalchemy import MetaData, Column, String, Integer
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import declarative_base

Base = declarative_base(metadata=MetaData())


class User(Base):
    __tablename__ = 'users'

    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid4())
    token = Column(String(), nullable=False)
    chat_id = Column(Integer())
    name = Column(String(), nullable=False)
