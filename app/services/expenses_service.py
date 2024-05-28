
from app.database import database_functions
from app.models.expense_model import Expense
from datetime import datetime
from app.models.user_model import User
from app import utils


async def get_expense_by_id(expense_id: int):
    try:
        expense = await database_functions.get_by_id("expenses",expense_id)
        if expense is None:
            raise ValueError("Expense not found")
        return expense
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_all_expenses_by_user_id(user_id: int):
    try:
        all_revenues = await database_functions.get_all_by_user_id("expenses",user_id)
        if not all_revenues :
            raise ValueError("Expenses not found")
        return all_revenues
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_expense(user_id, new_expense: Expense):
    try:
        new_expense.id = await utils.last_id("expenses") + 1
        new_expense.user_id = user_id
        user = await database_functions.get_by_id("users",user_id)
        if user is None:
            raise ValueError("User not found")
        user['balance'] -= new_expense.total_expense
        await database_functions.update("users",user)

        new_expense_dict = new_expense.dict()
        return await database_functions.add("expenses",new_expense_dict)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def update_expense(expense_id: int, new_expense: Expense):
    try:
        existing_expense = await get_expense_by_id(expense_id)
        last_user_id = existing_expense['user_id']
        last_total_expense = existing_expense['total_expense']

        user_data = await database_functions.get_by_id("users", last_user_id)
        user = User(**user_data)
        user.balance += last_total_expense
        await database_functions.update("users", user.dict())

        new_user_data = await database_functions.get_by_id("users", new_expense.user_id)
        new_user = User(**new_user_data)
        new_user.balance -= new_expense.total_expense
        await database_functions.update("users", new_user.dict())

        new_expense.id = expense_id
        new_expense.date = datetime.now()
        updated_revenue = new_expense.dict()
        return await database_functions.update("expenses", updated_revenue)
    except Exception as e:
        raise RuntimeError(f"Error updating expense: {e}")


async def delete_expense(expense_id):
    try:
        expense = await get_expense_by_id(expense_id)
        if not expense:
            raise ValueError(f"Expense with ID {expense_id} not found.")

        user_data = await database_functions.get_by_id("users", expense['user_id'])
        user = User(**user_data)
        user.balance += expense['total_expense']
        await database_functions.update("users", user.dict())

        await database_functions.delete("expenses", expense['id'])
        return f"Expense with ID {expense_id} deleted successfully."
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise RuntimeError(f"Error deleting expense: {e}")
