from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from app import Base

class Cat (Base):
    """
    テスト用モデルです．
    """
    __tablename__ = 'cat_information'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    breed = Column(String(255))
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, breed={self.breed}, created_at={self.created_at})>"