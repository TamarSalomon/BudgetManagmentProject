import uvicorn as uvicorn
from fastapi import FastAPI
from app.routes.users_router import user_router
import bcrypt


app = FastAPI()
app.include_router(user_router, prefix='/user')



if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)