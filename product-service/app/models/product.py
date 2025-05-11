from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class ProductCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = ""
    stock: int
    seller: Optional[str] = ""
    images: Optional[List[str]] = []
    category: Optional[str] = ""

class Product(ProductCreate):
    id: UUID
    created_at: datetime
