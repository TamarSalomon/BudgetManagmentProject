from bson import ObjectId

def to_json(data):
    if isinstance(data, list):
        return [to_json(item) for item in data]
    if isinstance(data, dict):
        return {key: to_json(value) for key, value in data.items()}
    if isinstance(data, ObjectId):
        return str(data)
    return data