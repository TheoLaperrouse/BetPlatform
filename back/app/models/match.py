
from sqlalchemy import ARRAY, Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Match(Base):
    __tablename__ = 'matches'

    id = Column(String, primary_key=True, unique=True, nullable=False)
    teams = Column(ARRAY(String), nullable=False)
    score = Column(ARRAY(Integer)) 
    match_date = Column(DateTime(timezone=True))
    match_day = Column(Integer) 
    is_home = Column(Boolean)
    link = Column(String)
    bets = relationship('Bet', back_populates='match')
    