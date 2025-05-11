from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID

from app.models.product import Product, ProductCreate
from app.services import product_service
from app.auth.dependencies import get_current_user, require_admin

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

# 🔐 Protected: any registered user
@router.post("/", response_model=Product, dependencies=[Depends(get_current_user)])
def create_product(product: ProductCreate, user: dict = Depends(get_current_user)):
    return product_service.create_product(product)

# 🔐 Protected: any registered user
@router.put("/{product_id}", response_model=Product, dependencies=[Depends(get_current_user)])
def update_product(product_id: UUID, product: ProductCreate, user: dict = Depends(get_current_user)):
    return product_service.update_product(product_id, product)

# 🔐 Optional: admin-only
@router.delete("/{product_id}", dependencies=[Depends(require_admin)])
def delete_product(product_id: UUID, user: dict = Depends(require_admin)):
    product_service.delete_product(product_id)
    return {"message": "Product deleted"}
