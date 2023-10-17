from pydantic import BaseModel
from typing import List

class MatchCreate(BaseModel):
    team1: str
    team2: str
    date: str
    is_home: bool
    score: int

class MatchList(BaseModel):
    matches: List[MatchCreate]
