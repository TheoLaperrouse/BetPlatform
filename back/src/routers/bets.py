from fastapi import APIRouter

router = APIRouter(
    prefix="/bets",
    tags=["bets"]
)

@router.get("/")
def get_bets():
    '''Get all the bets'''
    return []

@router.get("/{num_lic}")
def get_bets_by_player(num_lic):
    '''Get all bets by players'''
    return []
 
 
@router.post("/")
def post_bet():
    '''Post a bet for a match'''
    return {}

@router.put("/{id}")
def update_bet(id):
    '''Get all bets by players'''
    return {}
 