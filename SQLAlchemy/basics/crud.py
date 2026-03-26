from sqlalchemy.orm import Session
from fastapi import HTTPException
from SQLAlchemy.basics import models

def create_user(db:Session , user):
    existing_user=db.query(models.User).filter(models.User.id==user.id).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="ID already exists")
    user = models.User(name=user.name,age=user.age,id=user.id,email=user.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read(db:Session):
    user=db.query(models.User).all()
    return user

def update(db:Session , name:str , id:int,email:str , age:int):
    user=db.query(models.User).filter(models.User.id == id).first()
    if user:
        user.id=id
        user.name=name
        user.email=email
        user.age=age
        db.commit()
        db.refresh(user)
        return user
    return None

def delete(db:Session,id:int):
    user=db.query(models.User).filter(models.User.id==id).first()
    if user:
        db.delete(user)
        db.commit()
        return "delete successfully"
    return "user not found"