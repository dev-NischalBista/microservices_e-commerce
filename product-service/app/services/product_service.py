from app.db.client import supabase
from app.models.product import Product, ProductCreate
from uuid import UUID

def list_products():
    result = supabase.table("products").select("*").execute()
    return [Product(**item) for item in result.data]

def get_product_by_id(product_id: UUID):
    result = supabase.table("products").select("*").eq("id", str(product_id)).single().execute()
    if not result.data:
        return None
    return Product(**result.data)

def get_products_by_category(category: str):
    result = supabase.table("products").select("*").eq("category", category).execute()
    return [Product(**item) for item in result.data]

def create_product(product: ProductCreate):
    data = product.dict(exclude_unset=True)
    result = supabase.table("products").insert(data).execute()

    if not result.data:
        raise Exception("Failed to create product")

    return Product(**result.data[0])

def update_product(product_id: UUID, product: ProductCreate):
    data = product.dict(exclude_unset=True)
    result = supabase.table("products").update(data).eq("id", str(product_id)).execute()

    if not result.data:
        raise Exception("Failed to update product")

    return Product(**result.data[0])

def delete_product(product_id: UUID):
    result = supabase.table("products").delete().eq("id", str(product_id)).execute()

    if not result.data:
        raise Exception("Failed to delete product")

    return result.data
