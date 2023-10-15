from pydantic import BaseModel, UUID4

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class User(UserCreate):
    id: UUID4

class UserInDB(User):
    hashed_password: str