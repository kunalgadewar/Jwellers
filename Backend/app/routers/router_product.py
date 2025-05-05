# app/routers/router_product.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import schemas_product
from app.crud import crud_product
from app.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/", response_model=schemas_product.Product)
def create_product(product_in: schemas_product.ProductCreate, db: Session = Depends(get_db)):
    return crud_product.create_product(db, product_in)

@router.get("/", response_model=list[schemas_product.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_product.get_products(db, skip=skip, limit=limit)

@router.get("/{product_id}", response_model=schemas_product.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=schemas_product.Product)
def update_product(product_id: int, product_in: schemas_product.ProductCreate, db: Session = Depends(get_db)):
    updated = crud_product.update_product(db, product_id, product_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}", response_model=schemas_product.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted = crud_product.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted
 