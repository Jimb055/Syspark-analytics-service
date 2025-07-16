from sqlalchemy import Column, Integer, String
from app.database import Base

class Statistics(Base):
    __tablename__ = "statistics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
