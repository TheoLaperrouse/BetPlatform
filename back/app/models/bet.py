import uuid
from sqlalchemy import ARRAY, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID 
from app.database import Base
class Bet(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    user = relationship('User', back_populates='bets')
    match_id = Column(Integer, ForeignKey('matches.id'))
    match = relationship("Match", back_populates="bets")
    