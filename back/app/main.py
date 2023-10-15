import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routers import bets, users
from app.database import SessionLocal


def init_routers(_app):
    '''Initialize routers'''
    routers = [bets, users]
    for router in routers:
        _app.include_router(router.router)


app = FastAPI()

        
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

init_routers(app)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    '''Redirect to docs on /'''
    return RedirectResponse(url='/docs')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
