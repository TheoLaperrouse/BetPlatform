from fastapi import APIRouter, Depends, Header, HTTPException
from passlib.context import CryptContext
from sqlalchemy import text

from app.auth import JWTBearer, create_access_token, decodeJWT
from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserCredentials, UserUpdate

db = SessionLocal()
    
router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/",dependencies=[Depends(JWTBearer())])
def get_users():
    '''Get all users'''
    query = text("SELECT id, first_name, last_name FROM users")
    users_data = db.execute(query)
    users = []
    for user in users_data:
        id,first_name,last_name = user
        users.append({
            "id": id, 
            "first_name":first_name,
            "last_name":last_name,
            "correct_bets":0,
            "perfect_bets":0,
            "points":0
        })
    return users

@router.get("/me",dependencies=[Depends(JWTBearer())])
async def get_me(authorization: str = Header(None)):
    token = authorization.split("Bearer ")[1]
    user = decodeJWT(token)
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

@router.put("/{user_id}", dependencies=[Depends(JWTBearer())])
async def update_user(user_id: str, user_data: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    existing_user = User.get_by_email(db, user_data.email)
    if existing_user and user_data.email != db_user.email :
        raise HTTPException(status_code=409, detail="L'email est déjà associé à un utilisateur")
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur non trouvé")
    
    db_user.first_name = user_data.first_name
    db_user.last_name = user_data.last_name
    db_user.email = user_data.email
    if user_data.password and  user_data.password != '':
        db_user.password = pwd_context.hash(user_data.password)
    
    db.commit()

    access_token = create_access_token(data={"email": db_user.email, "id": str(db_user.id), "first_name": db_user.first_name, "last_name": db_user.last_name})
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