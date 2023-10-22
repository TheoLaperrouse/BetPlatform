import uuid
from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID 
from app.database import Base
class Bet(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    match_day = Column(Integer)
    match_id = Column(String, ForeignKey('matches.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    match = relationship("Match", back_populates="bets")
    user = relationship('User', back_populates='bets')