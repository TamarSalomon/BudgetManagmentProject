import pytest
from app.routes import users_router
from app.models.user_model import User


@pytest.mark.asyncio
async def test_get_all_users():
    """
    Test to retrieve all users.

    Retrieves all users and checks if the returned result is not None and is a list.
    """

    result = await users_router.get_all_users()
    assert result is not None
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_user_by_id():
    """
    Test to retrieve a user by their ID.

    Retrieves a user by their ID and checks if the returned result is not None,
    is a dictionary, and contains the correct user ID.
    """

    user_id = 2
    result = await users_router.get_user_by_id(user_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == user_id


@pytest.mark.asyncio
async def test_add_user():
    """
    Test to add a new user.

    Creates a new user object and adds it to the database. Checks if the returned result is not None,
    contains an 'inserted_id' key, and is a dictionary.
    """

    new_user = User(
        id=77379,
        name="test",
        password="Test1234a",
        email="test@example.com",
        phone="089745014",
        balance=0.0
    )
    result = await users_router.add_user(new_user)

    assert result is not None
    assert "inserted_id" in result
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_delete_user():
    """
    Test to delete a user by their ID.

    Deletes a user by their ID and checks if the returned result is not None, is a string,
    and contains the success message 'deleted successfully'.
    """

    user_id = 2
    result = await users_router.delete_user(user_id)
    assert result is not None
    assert isinstance(result, str)
    assert "deleted successfully" in result
