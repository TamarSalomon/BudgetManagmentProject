from bson import ObjectId

from app.database.database_connection import my_db

from app.utils import to_json
import json
from bson import json_util



async def get_all(collection_name):
    """
    Retrieves all documents from a specified collection.

    Args:
        collection_name (str): The name of the collection to retrieve documents from.

    Returns:
        list: A list of documents from the collection.
    """
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)  # Convert cursor to list
        return to_json(results)
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id(collection_name, object_id):
    try:
        user = await my_db[collection_name].find_one({"id": object_id})
        return to_json(user)
    except Exception as e:
        raise RuntimeError(f"Error cannot get this {object_id} object: {e}")




async def add_user(collection_name, document):
    try:
        result = await my_db[collection_name].insert_one(document)
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection_name}: {e}")
