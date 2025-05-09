from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class Product(BaseModel):
    id: Optional[UUID] = None
    name: str
    price: float
    description: Optional[str] = ""
    stock: int
    seller: Optional[str] = ""
    images: Optional[str] = ""
    category: Optional[str] = ""
    created_at: Optional[datetime] = None
