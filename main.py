from fastapi import FastAPI, Form, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional
import secrets
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

fake_users_db = {
    "testuser": User(username="testuser", password="testpassword")
}

class AuthHandler:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return plain_password == hashed_password

    @staticmethod
    def get_user(db, username: str):
        if username in db:
            user_dict = db[username].__dict__
            return User(**user_dict)
        return None

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token")
async def login_for_access_token(username: str = Form(...), password: str = Form(...)):
    user = AuthHandler.get_user(fake_users_db, username)
    if not user or not AuthHandler.verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {"sub": user.username}
    token = create_jwt_token(token_data)
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    return {"message": "You have access to this protected route", "username": username}
