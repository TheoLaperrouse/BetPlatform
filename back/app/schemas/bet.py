from pydantic import BaseModel
from typing import List, UUID

class BetCreate(BaseModel):
    user_id: UUID
    match_id: UUID
    team_selected: str

class Bet(BaseModel):
    id: UUID
    user_id: UUID
    match_id: UUID
    team_selected: str

class BetInResponse(BaseModel):
    bets: List[Bet]