from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    making_time = Column(String(100), nullable=False)
    serves = Column(String(100), nullable=False)
    ingredients = Column(String(300), nullable=False)
    cost = Column(Integer, nullable=False)

    # TIMESTAMP (DEFAULT CURRENT_TIMESTAMP)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
