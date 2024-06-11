from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from database import session, Engine
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Product
from schames import ProductSchames

session = session(bind=Engine)

product_router = APIRouter(prefix="/product")


@product_router.get("/")
async def list():
    products = session.query(Product).all()
    context = [
        {
            "id": product.id,
            "product_name": product.product_name,
            "photo": product.photo,
            "price": product.price,
            "description": product.description,
            "category_code": product.category_code,
            "category_name": product.category_name,
            "subcategory_code": product.subcategory_code,
            "subcategory_name": product.subcategory_name
        }
        for product in products
    ]
    return jsonable_encoder(context)


@product_router.post("/create")
async def create(product: ProductSchames):
    check_product = session.query(Product).filter(Product.id == product.id).first()
    if check_product:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bunday ma'lumot mavjud")
    new_product = Product(
        id=product.id,
        product_name=product.product_name,
        photo=product.photo,
        price=product.price,
        description=product.description,
        category_code=product.category_code,
        category_name=product.category_name,
        subcategory_code=product.subcategory_code,
        subcategory_name=product.subcategory_name,
    )
    session.add(new_product)
    session.commit()
    data = {
        "code": 201,
        "msg": "Successfully",
        "Product": {
            "id": product.id,
            "name": product.product_name,
            "price": product.price,
            "count": product.description
        }
    }

    return data
