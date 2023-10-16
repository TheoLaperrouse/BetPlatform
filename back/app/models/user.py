
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID 
from app.database import Base
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, index=True, unique=True, nullable=False)
    password = Column(String)
    bets = relationship("Bet", back_populates="user")
    
    @classmethod
    def get_by_email(cls, db, email: str):
        return db.query(cls).filter(cls.email == email).first()
