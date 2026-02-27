from fastapi import APIRouter, HTTPException
from db import get_connection
from schemas import UserCreate, TodoCreate
from passlib.context import CryptContext
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/register")
def register(user: UserCreate):
    conn = get_connection()
    cur = conn.cursor()

    hashed_password = pwd_context.hash(user.password)

    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (user.username, hashed_password)
        )
        conn.commit()
    except:
        raise HTTPException(status_code=400, detail="User already exists")

    cur.close()
    conn.close()

    return {"message": "User registered successfully"}

@router.post("/login")
def login(user: UserCreate):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=%s", (user.username,))
    db_user = cur.fetchone()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not pwd_context.verify(user.password, db_user[2]):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})

    return {"access_token": token}