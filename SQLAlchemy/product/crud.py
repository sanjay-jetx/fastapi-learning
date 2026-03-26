from sqlalchemy.orm import Session
from fastapi import HTTPException
from .models import Product

def create_product(db:Session,product):
    existing_product=db.query(Product).filter(Product.id == product.id).first()
    if existing_product:
        raise HTTPException(status_code=400,detail="Product exists")
    


    new_product=Product(
        id=product.id,
        name=product.name,
        price=product.price,
        quantity=product.quantity
        

    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


def Display_Product(db:Session):
    product = db.query(Product).all()

    return product


def Update(db:Session,new_product):
    product=db.query(Product).filter(Product.id==new_product.id).first()
    if product:
        product.name = new_product.name
        product.price = new_product.price
        product.quantity = new_product.quantity
        db.commit()
        db.refresh(product)
        return product
    return None


def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()

    if product:
        db.delete(product)
        db.commit()
        return "successfully deleted"

    return "product not found"