# app/models/product.py

from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)  # e.g., gold, silver, platinum, stone
    type = Column(String(50), nullable=False)      # e.g., ring, necklace
    description = Column(String(255))
    price_per_gram = Column(Float, nullable=False)
    rating = Column(Float)
    image_url = Column(String(255))
