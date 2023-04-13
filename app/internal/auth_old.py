#System imports
import hashlib

#Libs imports
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from routers.users import users

#Local imports

router = APIRouter()

def sha256_hash_bytes(string):
    return hashlib.sha256(bytes(string, encoding='utf8')).digest()

def hash_password(password: str):
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    for user in users:
        if user["name"] == form_data.username:
            if user["password_hash"] == hash_password(form_data.password):
                return {"access_token": user["name"], "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect username or password")


