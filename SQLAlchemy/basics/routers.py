from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud
from SQLAlchemy.basics.database import get_db
from SQLAlchemy.basics.schemas import UserCreate

router=APIRouter()

@router.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return crud.read(db)


@router.put("/users/{id}")
def update_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = crud.update(db, user.name, id, user.email, user.age)

    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")

    return updated_user


@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    result = crud.delete(db, id)
    return {"message": result}