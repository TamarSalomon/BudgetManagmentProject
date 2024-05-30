from app.database.database_connection import my_db


async def get_all(collection_name):
    """
    Retrieves all documents from the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.

    Returns:
        list: A list of dictionaries, each containing information about a document.
    """
    from app.utils import to_json
    try:
        cursor = my_db[collection_name].find({})
        results = await cursor.to_list(length=None)
        return to_json(results)
    except Exception as e:
        raise RuntimeError(f"Error retrieving documents from collection {collection_name}: {e}")


async def get_by_id(collection_name, object_id):
    """
    Retrieves a document by its ID from the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.
        object_id (int): The ID of the document to retrieve.

    Returns:
        dict: A dictionary containing the document's information.
    """
    from app.utils import to_json
    try:
        element = await my_db[collection_name].find_one({"id": object_id})
        if element is None:
            raise ValueError("Element not found")
        return to_json(element)
    except Exception as e:
        raise RuntimeError(f"Error retrieving document: {e}")


async def get_all_by_user_id(collection_name, user_id):
    """
    Retrieves all documents for a specific user by their user ID from the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.
        user_id (int): The ID of the user whose documents are to be retrieved.

    Returns:
        list: A list of dictionaries, each containing information about a document.
    """
    try:
        all_items = await my_db[collection_name].find({"user_id": user_id}).to_list(length=None)
        for item in all_items:
            item["_id"] = str(item["_id"])
        return all_items
    except Exception as e:
        raise RuntimeError(f"Error retrieving items by user ID: {e}")


async def add(collection_name, object):
    """
    Adds a new document to the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.
        object (dict): A dictionary containing the document's information.

    Returns:
        dict: A dictionary containing the inserted document's ID.
    """
    try:
        result = await my_db[collection_name].insert_one(object)
        return {"inserted_id": str(result.inserted_id)}
    except Exception as e:
        raise RuntimeError(f"Error adding document to collection {collection_name}: {e}")


async def update(collection_name, object):
    """
    Updates a document in the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.
        object (dict): The updated document.

    Returns:
        str: A message indicating the success of the update.
    """
    try:
        existing_object = await get_by_id(collection_name, object['id'])
        if existing_object:
            new_object = {key: value for key, value in object.items() if key != '_id'}
            await my_db[collection_name].update_one({"id": object['id']}, {"$set": new_object})
            return f"Document with ID {object['id']} updated successfully."
        else:
            raise ValueError(f"No document found with ID {object['id']}.")
    except Exception as e:
        raise RuntimeError(f"Error updating document: {e}")


async def delete(collection_name, object_id):
    """
    Deletes a document by its ID from the specified collection.

    Args:
        collection_name (str): The name of the collection in the database.
        object_id (int): The ID of the document to delete.

    Returns:
        str: A message indicating the success of the deletion.
    """
    try:
        result = await my_db[collection_name].delete_one({"id": object_id})
        if result.deleted_count > 0:
            return f"Document with ID {object_id} deleted successfully."
        else:
            raise ValueError(f"No document found with ID {object_id}.")
    except Exception as e:
        raise RuntimeError(f"Error deleting document: {e}")
