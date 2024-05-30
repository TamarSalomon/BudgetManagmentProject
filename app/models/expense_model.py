from datetime import datetime

from pydantic import BaseModel, validator

from app.validition import validition_functions


class Expense(BaseModel):
    id: int
    user_id: int
    total_expense: float
    date: datetime

    @validator('total_expense')
    def validate_total_expense(cls, total_expense):
        return validition_functions.is_valid_amount(total_expense)
