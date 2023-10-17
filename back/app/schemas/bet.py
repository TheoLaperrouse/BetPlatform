from pydantic import BaseModel

class BetBase(BaseModel):
    match_day: int
    teams: str
    user_id: int

class BetCreate(BetBase):
    pass

class BetUpdate(BetBase):
    pass

class Bet(BetBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True