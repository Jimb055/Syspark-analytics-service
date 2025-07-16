from pydantic import BaseModel

class StatisticsResponse(BaseModel):
    total_users: int
    total_boards: int
    pending_tasks: int
    completed_tasks: int