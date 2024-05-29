
from app.database import database_functions
from app.models.expense_model import Expense
from datetime import datetime
from app.models.user_model import User
from app import utils




async def get_all_expenses_by_user_id(user_id: int):
    """
        Retrieve all expenses for a specific user.
        Args:
            user_id (int): The ID of the user.
        Returns:
            List[Expense]: A list of expenses for the user.
        Raises:
            ValueError: If no expenses are found for the user.
            Exception: For any other unexpected errors.
        """
    try:
        all_expenses = await database_functions.get_all_by_user_id("expenses",user_id)
        if not all_expenses :
            raise ValueError("Expenses not found")
        return all_expenses
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def get_expense_by_id(expense_id: int):
    """
       Retrieve an expense by its ID.
       Args:
           expense_id (int): The ID of the expense to retrieve.
       Returns:
           Expense: The expense object if found.
       Raises:
           ValueError: If the expense is not found.
           Exception: For any other unexpected errors.
       """
    try:
        expense = await database_functions.get_by_id("expenses",expense_id)
        if expense is None:
            raise ValueError("Expense not found")
        return expense
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def create_expense(user_id, new_expense: Expense):
    """
        Create a new expense entry for a user.
        Args:
            user_id (int): The ID of the user.
            new_expense (Expense): The expense object containing expense details.
        Returns:
          dict: A dictionary containing the inserted ID as a string.
        Raises:
            ValueError: If the user is not found.
            Exception: For any unexpected errors during expense creation.
        """
    try:
        new_expense.id = await utils.last_id("expenses") + 1
        new_expense.user_id = user_id
        user = await database_functions.get_by_id("users",user_id)
        if user is None:
            raise ValueError("Expense not found")
        user['balance'] -= new_expense.total_expense
        await database_functions.update("users",user)

        new_expense_dict = new_expense.dict()
        return await database_functions.add("expenses",new_expense_dict)
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise e


async def update_expense(expense_id: int, new_expense: Expense):
    """
       Update an existing expense entry.
       Args:
           expense_id (int): The ID of the expense to update.
           new_expense (Expense): The expense object containing updated details.
       Returns:
          str: Success message indicating the expense was updated.
       Raises:
           Exception: For any unexpected errors during expense update.
       """
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
            raise e



async def delete_expense(expense_id):
    """
    Delete an expense entry and update the user's balance accordingly.
    Args:
        expense_id (int): The ID of the expense to delete.
    Returns:
        str: Success message indicating the expense was deleted.
    Raises:
        ValueError: If the expense is not found.
        Exception: For any other unexpected errors.
    """
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
        raise e

