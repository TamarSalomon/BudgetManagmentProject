import uvicorn as uvicorn
from fastapi import FastAPI
from app.routes.users_router import user_router
from app.routes.visualization_router import visualization_router
from app.routes.expenses_router import expense_router
from app.routes.revenues_router import revenue_router



import bcrypt


app = FastAPI()
app.include_router(user_router, prefix='/users')
app.include_router(visualization_router, prefix="/visualization")
app.include_router(revenue_router, prefix="/revenues")
app.include_router(expense_router, prefix="/expenses")




if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8001)