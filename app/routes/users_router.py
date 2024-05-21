# app/routes/userRouter.py
from fastapi import APIRouter, HTTPException
from app.models.user_model import User
from app.services import users_service
import json
from bson import json_util

userRouter = APIRouter()

@userRouter.get('/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        return await users_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@userRouter.get('/')
async def get_all_users():
    try:
        return await users_service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@userRouter.post('/')
async def add_user(new_user: User):
    try:
        return await users_service.create_user(new_user.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))