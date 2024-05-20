import uvicorn as uvicorn
from fastapi import FastAPI
from app.routes.userRouter import userRouter
app = FastAPI()
app.include_router(userRouter, prefix='/user')

@app.get("/")
async def root():
    return {"messege":"nfjnfj"}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)