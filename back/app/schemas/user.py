from pydantic import BaseModel, UUID4
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    
class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: Optional[str]
    
class User(UserCreate):
    id: UUID4
    
class UserCredentials(BaseModel):
    email: str
    password: str
