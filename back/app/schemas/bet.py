from typing import List

from pydantic import BaseModel


class BetBase(BaseModel):
    bet_score: int
    match_id: str
    user_id: int


class BetCreate(BaseModel):
    bet_score: List[int]
    match_id: str


class BetUpdate(BaseModel):
    bet_score: List[int]
