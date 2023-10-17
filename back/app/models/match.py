from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, index=True)
    teams = Column(ARRAY(String), nullable=False)
    score = Column(ARRAY(String), default=0)
    match_id = Column(Integer, ForeignKey('matches.id'))
    is_home = Column(Boolean)
    link = Column(String)
    bets = relationship("Bet", back_populates="match")