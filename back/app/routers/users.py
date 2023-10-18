from fastapi import APIRouter, HTTPException, Header
from app.schemas.user import UserCreate, UserCredentials
from app.models.user import User
from passlib.context import CryptContext
from app.auth import create_access_token, verify_token
from app.database import SessionLocal

db = SessionLocal()
    
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/")
def get_users():
    '''Get all users'''
    users = db.query(User).all().copy()
    for user in users:
        if user.password:
            del user.password
        user.correct_bets = 0
        user.perfect_bets = 0
        user.points =  user.perfect_bets * 2 +  user.correct_bets
    return sorted(users, key=lambda user: user.points, reverse=True)

@router.get("/me")
async def get_me(authorization: str = Header(None)):
    if authorization:
        token = authorization.split("Bearer ")[1]
        user = verify_token(token)
    else:
        raise HTTPException(status_code=401, detail="Pas de headers Authorization envoyé")
    if user is None:
        raise HTTPException(status_code=401, detail="Invalide ou expiré token")
    return user

@router.post("/")
async def create_user(user: UserCreate):
    existing_user = User.get_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="L'email est déjà associé à un utilisateur")
    user.password = pwd_context.hash(user.password)  
    
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    access_token = create_access_token(data={"email": db_user.email,"id": str(db_user.id), "first_name": db_user.first_name, "last_name": db_user.last_name})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login")
async def login(user: UserCredentials):
    db_user = User.get_by_email(db, user.email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="L'email ne correspond à aucun utilisateur")
    
    if not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Mot de passe incorrect")
    
    access_token = create_access_token(data={"email": db_user.email,"id": str(db_user.id), "first_name": db_user.first_name, "last_name": db_user.last_name})
    return {"access_token": access_token, "token_type": "bearer"}