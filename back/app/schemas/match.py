from pydantic import BaseModel
from typing import List

class MatchCreate(BaseModel):
    teams: List[str]
    date: str
    is_home: bool
    score: int

class MatchList(BaseModel):
    matches: List[MatchCreate]
