from fastapi import APIRouter, Depends, Header, HTTPException

from app.auth import JWTBearer, decodeJWT
from app.database import SessionLocal
from app.models.bet import Bet
from app.schemas.bet import BetCreate

db = SessionLocal()

router = APIRouter(
    prefix="/bets",
    tags=["bets"]
)

@router.get("",dependencies=[Depends(JWTBearer())])
def get_bets():
    '''Get all the bets'''
    bets = db.query(Bet).all()
    return bets

@router.get("/my_bets",dependencies=[Depends(JWTBearer())])
def get_my_bets(authorization: str = Header(None)):
    '''Get my bets'''
    token = authorization.split("Bearer ")[1]
    user = decodeJWT(token)
    bets = db.query(Bet).filter(Bet.user_id == user['id'])
    return bets

@router.post("/", dependencies=[Depends(JWTBearer())])
def create_bet(bet_data: BetCreate, authorization: str = Header(None)):
    '''Create a bet'''
    token = authorization.split("Bearer ")[1]
    user = decodeJWT(token)
    bet = {"match_id":bet_data.match_id, "bet_score":bet_data.bet_score, "user_id": user['id']}
    db_bet = Bet(**bet)
    db.add(db_bet)
    db.commit()
    db.refresh(db_bet)
    return db_bet

@router.put("/{bet_id}",  dependencies=[Depends(JWTBearer())])
def update_bet(bet_id: int, bet_data: BetCreate):
    '''Update a bet'''
    db_bet = db.query(Bet).filter(Bet.id == bet_id).first()
    if not db_bet:
        raise HTTPException(status_code=404, detail="Pari non trouvé")
    
    for key, value in bet_data.model_dump().items():
        setattr(db_bet, key, value)

    db.commit()
    db.refresh(db_bet)
    return db_bet


