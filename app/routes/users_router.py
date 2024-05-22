# app/routes/userRouter.py
from fastapi import APIRouter, HTTPException
from app.models.user_model import User
from app.services import users_service
import json
from bson import json_util

user_router = APIRouter()



@user_router.get('/')
async def get_all_users():
    try:
        return await users_service.get_all_users()
    except ValueError as e:
       raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        return await users_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.post('/register')
async def add_user(new_user: User):
    try:
        return await users_service.create_user(new_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.post('/login')
async def login_user(user_name: str ,user_password:str):
    try:
        return await users_service.login_user(user_name,user_password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@user_router.put('/{user_id}')
async def update_user(user_id: int, user_update: User):
    try:
        return await users_service.update_user(user_id, user_update)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

