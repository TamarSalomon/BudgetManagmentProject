from app.validition import validition_functions
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    name: str
    password: str
    email: str
    phone: str
    balance: float

    @validator('name')
    def validate_name(cls, name):
        return validition_functions.is_valid_name(name)

    @validator('email')
    def validate_email(cls, email):
        return validition_functions.is_valid_email(email)

    @validator('password')
    def validate_password(cls, password):
        return validition_functions.is_valid_password(password)

    @validator('phone')
    def validate_phone(cls, phone):
        return validition_functions.is_valid_phone(phone)
