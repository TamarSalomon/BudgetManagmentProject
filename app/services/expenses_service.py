from app.database import database_functions
from app.models.expense_model import Expense

async def create_expenses(new_expense: Expense):
    try:
        new_expense = new_expense.dict()
        user = await database_functions.get_by_id("users",new_expense['user_id'])
        if user['balance'] < new_expense['user_id']:
            raise ValueError("You don't have enough money in your account")
        user['balance'] = user['balance'] - new_expense['total_expense']
        return await database_functions.add("expenses",new_expense)
    except Exception as e:
        raise e


