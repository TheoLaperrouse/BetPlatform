import uuid
from sqlalchemy import Column, Integer, String, ARRAY, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID 
class Match(Base):
    __tablename__ = 'matches'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    teams = Column(ARRAY(String), nullable=False)
    score = Column(ARRAY(Integer)) 
    match_date = Column(DateTime(timezone=True))
    match_day = Column(Integer) 
    is_home = Column(Boolean)
    link = Column(String, unique=True)
    bets = relationship('Bet', back_populates='match')
    