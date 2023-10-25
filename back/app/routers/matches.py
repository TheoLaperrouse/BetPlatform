from fastapi import APIRouter, Depends

from app.auth import JWTBearer
from app.database import SessionLocal
from app.models.match import Match

db = SessionLocal()

router = APIRouter(
    prefix="/matches",
    tags=["matches"]
)

@router.get("", dependencies=[Depends(JWTBearer())])
def get_matches():
    '''Get all matches'''
    matches = db.query(Match).all()
    return matches
