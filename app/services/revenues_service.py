from app.database import database_functions
from app.models.revenue_model import Revenue


async def create_revenue(new_revenue: Revenue):
    try:
        existing_revenue = await get_revenue_by_id(new_revenue.id)
        if existing_revenue:
            raise ValueError("revenue already exists")

        new_revenue = new_revenue.dict()
        user = await database_functions.get_by_id("users", new_revenue['user_id'])
        user['balance'] += new_revenue['total_revenue']
        await  database_functions.update("users",user)
        return await database_functions.add("revenues", new_revenue)
    except Exception as e:
        raise e

async  def get_revenue_by_id(revenue_id):
    try:
        revenue=await database_functions.get_by_id("revenues",revenue_id)
        if revenue is None:
            raise ValueError("revenue not found")
    except ValueError as ve:
            raise ve
    except Exception as e:
        raise e
