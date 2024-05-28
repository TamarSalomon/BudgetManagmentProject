from bson import ObjectId

from app.database.database_functions import get_all


def to_json(data):
    if isinstance(data, list):
        return [to_json(item) for item in data]
    if isinstance(data, dict):
        return {key: to_json(value) for key, value in data.items()}
    if isinstance(data, ObjectId):
        return str(data)
    return data


async def last_id(collection_name):
    """
    Retrieves the last ID from a specified collection in the database.

    Args:
        collection_name (str): The name of the collection in the database.

    Returns:
        int: The last ID found in the collection.
    """
    try:
        all_collection = await get_all(collection_name)
        if not all_collection:
            return -1
        max_id = max(item.get('id', 0) for item in all_collection)
        return max_id
    except Exception as e:
        raise RuntimeError(f"Error retrieving last ID: {e}")