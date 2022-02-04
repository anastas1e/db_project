import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from schemas import CreateUserRequest, AddBookRequest
from sqlalchemy.orm import Session
from database import get_db
from models import User, Book

app = FastAPI()


@app.post("/user")
def create_user(details: CreateUserRequest, db: Session = Depends(get_db)):
    to_create = User(
        full_name=details.full_name,
        username=details.username,
        password=details.password,
    )
    user_exists = db.query(User).filter(User.username == to_create.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Sorry, user with this username already exists!")
    db.add(to_create)
    db.commit()
    return {"success": True, "createdUserId": to_create.id}


@app.post("/book")
def add_book(details: AddBookRequest, db: Session = Depends(get_db)):
    to_add = Book(
        title=details.title,
        author=details.author,
        description=details.description,
    )
    db.add(to_add)
    db.commit()
    return {"success": True, "createdBookId": to_add.id}


@app.get("/users/{id}")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == id).first()


@app.get("/")
def get_all(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.delete("/users/{id}")
def delete_by_id(id: int, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == id).delete()
    db.commit()
    return f"User with id {id} was deleted"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
