from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.ext.declarative import declarative_base
from app import Base

class Bet(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    match_day = Column(Integer)
    teams = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User', back_populates='bets')
    