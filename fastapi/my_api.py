from fastapi import FastAPI
from database import sessionmaker, engine, Base
from model import User

app=FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/users/")
def create_user(user:User):
    db=sessionmaker()
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user 

@app.get("/users/{user_id}")
def read_user(user_id:int):
    db=sessionmaker()
    user=db.query(User).filter(User.id==user_id).first()
    db.close()
    return user

