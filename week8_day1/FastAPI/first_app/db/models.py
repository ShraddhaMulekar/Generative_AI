from sqlalchemy import Boolean, Column, Integer, String
from db.database import Base

class test(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(String, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    in_stock = Column(Boolean, nullable=True)