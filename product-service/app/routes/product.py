from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID

from app.models.product import Product
from app.services import product_service

router = APIRouter()

@router.get("/", response_model=List[Product])
def list_products():
    return product_service.list_products()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: UUID):
    product = product_service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.get("/category/{category}", response_model=List[Product])
def get_by_category(category: str):
    return product_service.get_products_by_category(category)

@router.post("/", response_model=Product)
def create_product(product: Product):
    try:
        return product_service.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: UUID, product: Product):
    try:
        return product_service.update_product(product_id, product)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{product_id}")
def delete_product(product_id: UUID):
    try:
        product_service.delete_product(product_id)
        return {"message": "Product deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
