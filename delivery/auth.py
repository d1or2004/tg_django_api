from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from database import session, Engine
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Users
from schames import RegisterSchema

session = session(bind=Engine)

auth_router = APIRouter(prefix="/auth")


@auth_router.get('/')
async def list():
    users = session.query(Users).all()
    context = [
        {
            "id": user.id,
            "full_name": user.full_name,
            "username": user.username,
            "telegram_id": user.telegram_id
        }
        for user in users
    ]
    return jsonable_encoder(context)

