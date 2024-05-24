from datetime import datetime

from pydantic import BaseModel


class Revenue(BaseModel):
    id:int
    user_id: int
    total_revenue: float
    date: datetime
