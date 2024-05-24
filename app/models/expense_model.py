from datetime import datetime

from pydantic import BaseModel


class Expense(BaseModel):
    id:int
    user_id: int
    total_expense: float
    date: datetime
