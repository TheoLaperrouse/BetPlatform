from typing import List

from pydantic import BaseModel

from back.app.schemas.bet import BetBase


class Match(BaseModel):
    id: str
    teams: List[str]
    date: str
    is_home: bool
    score: int
    bets:List(BetBase)

class MatchList(BaseModel):
    matches: List[Match]
