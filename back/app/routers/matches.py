from fastapi import APIRouter
from app.schemas.match import MatchCreate, MatchList
from app.models.match import Match
from app.database import SessionLocal

db = SessionLocal()

router = APIRouter(
    prefix="/matches",
    tags=["matches"]
)

@router.get("/",response_model=MatchList)
def get_matches():
    '''Get all matches'''
    matches = db.query(Match).all()
    return matches

@router.post("/", response_model=MatchCreate)
async def create_match(match: MatchCreate):
    db_match = Match(**match.model_dump())
    db.add(db_match)
    db.commit()
    db.refresh(db_match)
    return db_match