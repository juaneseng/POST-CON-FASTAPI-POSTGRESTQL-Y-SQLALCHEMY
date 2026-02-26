from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from v1.models.create_product_model import Product
from v1.schema.create_product import CreateProductSchema
from v1.db.database import get_db

router = APIRouter(prefix="/products")

@router.post("/")
def create_product(product: CreateProductSchema, db: Session = Depends(get_db)):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"mensaje": "Producto creado correctamente "}


@router.get("/")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get("/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == id).first()

@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == id).delete()
    db.commit()
    return {"mensaje": "Producto eliminado correctamente "}
@router.put("/{id}")

def update_product(id: int, product: CreateProductSchema, db: Session = Depends(get_db)):
    db.query(Product).filter(Product.id == id).update(product.dict())
    db.commit()
    return {"mensaje": "Producto actualizado correctamente "}
