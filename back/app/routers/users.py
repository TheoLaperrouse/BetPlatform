from fastapi import APIRouter
from app.schemas.user import User
from passlib.context import CryptContext
from app.database import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/")
def get_users():
    '''Get all users'''
    return []

@router.post("/users/", response_model=User)
def create_user(user: User):
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        hashed_password=pwd_context.hash(user.password)
    )

    db = SessionLocal()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user