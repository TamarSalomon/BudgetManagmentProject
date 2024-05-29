import pytest
from app.routes import revenues_router
from app.models.revenue_model import Revenue


@pytest.mark.asyncio
async def test_get_all_revenues():
    """
    Test to retrieve all revenues for a user.

    Retrieves all revenues for a specific user ID and checks if the returned result is not None and is a list.
    """

    user_id = 13
    result = await revenues_router.get_all_revenues_by_user_id(user_id)
    assert result is not None
    assert isinstance(result, list)


@pytest.mark.asyncio
async def test_get_revenue_by_id():
    """
    Test to retrieve a revenue by its ID.

    Retrieves a revenue by its ID and checks if the returned result is not None,
    is a dictionary, and contains the correct revenue ID.
    """

    revenue_id = 21
    result = await revenues_router.get_revenue_by_id(revenue_id)
    assert result is not None
    assert isinstance(result, dict)
    assert result["id"] == revenue_id


@pytest.mark.asyncio
async def test_add_revenue():
    """
    Test to add a new revenue entry.

    Creates a new revenue object and adds it to the database. Checks if the returned result is not None,
    contains an 'inserted_id' key, and is a dictionary.
    """

    new_revenue = Revenue(
        id=1,
        user_id=13,
        total_revenue=100.0,
        date="2024-06-01T00:00:00Z"
    )
    result = await revenues_router.add_revenue(new_revenue.user_id, new_revenue)

    assert result is not None
    assert "inserted_id" in result
    assert isinstance(result, dict)
