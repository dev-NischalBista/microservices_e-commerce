from fastapi import FastAPI
from app.routes import product

app = FastAPI(title="Product Service")

app.include_router(product.router, prefix="/products", tags=["Products"])

# @app.get("/")
# def root():
#     return {"message": "Welcome to Product Service"}
