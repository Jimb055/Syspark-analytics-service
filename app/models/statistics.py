from sqlalchemy import Column, Integer, String
from app.database import Base
from pydantic import BaseModel

# SQLAlchemy model (Database)
class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

# Pydantic model (Response schema)
class StatisticsResponse(BaseModel):
    id: int
    name: str
    value: int

    class Config:
        orm_mode = True
