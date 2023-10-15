
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID 

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True, unique=True, nullable=False)
    hashed_password = Column(String)
