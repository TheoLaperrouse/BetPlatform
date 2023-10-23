import uuid

from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Bet(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    match_id = Column(String, ForeignKey('matches.id'))
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'))
    bet_score = Column(ARRAY(Integer)) 
    status = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    match = relationship("Match", back_populates="bets")
    user = relationship('User', back_populates='bets')