import pytest
from app.routes import expenses_router
from app.models.expense_model import Expense


@pytest.mark.asyncio
async def test_get_all_expenses():
    """
    Test to retrieve all expenses for a user.

    Retrieves all expenses for a specific user ID and checks if the returned result is not None and is a list.
    """

    user_id = 13
    result = await expenses_router.get_all_expenses_by_user_id(user_id)
    assert result is not None
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_expense_by_id():
    """
    Test to retrieve an expense by its ID.

    Retrieves an expense by its ID and checks if the returned result is not None,
    is a dictionary, and contains the correct expense ID.
    """

    expense_id = 0
    result = await expenses_router.get_expense_by_id(expense_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == expense_id


@pytest.mark.asyncio
async def test_add_expense():
    """
    Test to add a new expense entry.

    Creates a new expense object and adds it to the database. Checks if the returned result is not None,
    contains an 'inserted_id' key, and is a dictionary.
    """

    new_expense = Expense(
        id=1,
        user_id=13,
        total_expense=100.0,
        date="2024-06-01"
    )
    result = await expenses_router.add_expense(new_expense.user_id, new_expense)

    assert result is not None
    assert "inserted_id" in result
    assert isinstance(result, dict)
