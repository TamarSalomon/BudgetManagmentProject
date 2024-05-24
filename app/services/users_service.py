# app/services/userService.py
from fastapi import HTTPException


from app.models.user_model import User
from app.database.database_connection import my_db
from app.database import database_functions
async def get_all_users():
    try:
        return await database_functions.get_all("users")
    except Exception as e:
        raise e
async def get_user_by_id(user_id):
    try:
     user= await database_functions.get_by_id("users", user_id)
     if user is None:
        raise ValueError("user not found")
    except ValueError as ve:
        raise ve
    except Exception as e:
         raise e

async def create_user(new_user: User):
    try:
        new_user.id = await last_id() + 1
        new_user.balance = 0.0
        user = new_user.dict()
        return await database_functions.add("users",user)
    except Exception as e:
        raise e


async def update_user(user_id: int, user_update: User):
    try:
        existing_user = await get_user_by_id(user_id)
        if existing_user is None:
            raise ValueError("User not exists")
        user_update.balance = existing_user['balance']
        user_update.id = user_id
        user = user_update.dict()
        return await database_functions.update("users",user)
    except Exception as e:
        raise e

async  def login_user(user_name, user_password):
    try:
       return  await database_functions.login("users",user_name,user_password)
    except Exception as e:
        raise e





async def last_id():
    try:
        all_users = await get_all_users()
        max_id = 0
        for user in all_users:
            if user['id'] > max_id:
                max_id = user['id']
        return max_id
    except Exception as e:
        raise e


