from app.validition import validition_functions
from pydantic import BaseModel, validator

class User(BaseModel):
    id:int
    name: str
    password:str
    email:str
    phone:str
    balance:float



    @validator('name')
    def validate_name(cls, v):
        return validition_functions.is_valid_name(v)

    @validator('email')
    def validate_email(cls, v):
        return validition_functions.is_valid_email(v)
    @validator('password')
    def validate_password(cls, v):
        return validition_functions.is_valid_password(v)

    @validator('phone')
    def validate_phone(cls, v):
        return validition_functions.is_valid_phone(v)
