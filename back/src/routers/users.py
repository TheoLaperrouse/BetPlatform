from fastapi import APIRouter

router = APIRouter(
    prefix="/players",
    tags=["players"]
)

@router.get()
def get_players():
    '''Get all the bets'''
    return
