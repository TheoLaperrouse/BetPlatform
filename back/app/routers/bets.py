from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models.bet import Bet
from app.schemas.bet import BetCreate, BetUpdate
from app.database import SessionLocal

db = SessionLocal()

router = APIRouter(
    prefix="/bets",
    tags=["bets"]
)

@router.get("/")
def get_bets():
    '''Get all the bets'''
    bets = db.query(Bet).all()
    return bets

@router.get("/{bet_id}")
def get_bet(bet_id: int):
    '''Get a bet'''
    bet = db.query(Bet).filter(Bet.id == bet_id).first()
    if not bet:
        raise HTTPException(status_code=404, detail="Pari non trouvé")
    return bet

@router.post("/")
def create_bet(bet: BetCreate):
    '''Create a bet'''
    db_bet = Bet(**bet.model_dump())
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

@router.put("/{bet_id}")
def update_bet(bet_id: int, bet_data: BetUpdate):
    '''Update a bet'''
    db_bet = db.query(Bet).filter(Bet.id == bet_id).first()
    if not db_bet:
        raise HTTPException(status_code=404, detail="Pari non trouvé")
    
    for key, value in bet_data.model_dump().items():
        setattr(db_bet, key, value)

    db.commit()
    db.refresh(db_bet)
    return db_bet


