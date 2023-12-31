import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.database import engine
from app.models.bet import Bet
from app.models.match import Match
from app.models.user import User
from app.routers import bets, matches, users


def init_routers(_app):
    '''Initialize routers'''
    routers = [bets, users, matches]
    for router in routers:
        _app.include_router(router.router)


app = FastAPI()

        
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Match.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)
Bet.metadata.create_all(bind=engine)

init_routers(app)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    '''Redirect to docs on /'''
    return RedirectResponse(url='/docs')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
