from fastapi import APIRouter
from app.schemas.match import MatchCreate
from app.models.match import Match
from app.database import SessionLocal

db = SessionLocal()

router = APIRouter(
    prefix="/matches",
    tags=["matches"]
)

@router.get("/")
def get_matches():
    '''Get all matches'''
    matches = db.query(Match).all()
    return matches
