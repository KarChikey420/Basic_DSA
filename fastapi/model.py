from pydantic import BaseModel
from sqlalchemy import Column , Integer, String

class User(BaseModel):
    id: int 
    username: str
    email: str
    password: str
