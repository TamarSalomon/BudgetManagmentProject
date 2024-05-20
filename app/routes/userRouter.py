from fastapi import FastAPI, Depends, APIRouter, HTTPException
from http.client import HTTPException
import uvicorn
from fastapi_cli.cli import app

userRouter = APIRouter()


# @userRouter.get('/all')
# async def get_all_users():
#     return await "user_CRUD.get_all_users()"


tasks = []

@userRouter.get("/tasks")
async def get_Tasks():
    if not tasks:
        raise ValueError('error the array tasks is empty')
    return tasks