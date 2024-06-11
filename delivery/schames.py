from pydantic import BaseModel, Field, constr, condecimal
from typing import Optional
from decimal import Decimal


class ProductSchames(BaseModel):
    id: Optional[int]
    product_name: constr(max_length=50) = Field(..., example="Example Product")
    photo: Optional[constr(max_length=200)] = Field(None, example="file_id")
    price: condecimal(max_digits=200, decimal_places=2) = Field(..., example=99.99)
    description: constr(max_length=300) = Field(..., example="Product description")
    category_code: constr(max_length=200) = Field(..., example="CAT123")
    category_name: constr(max_length=200) = Field(..., example="Category Name")
    subcategory_code: constr(max_length=34) = Field(..., example="Subcategory Kod")
    subcategory_name: constr(max_length=30) = Field(..., example="Subcategory Name")


class RegisterSchema(BaseModel):
    id: Optional[int]
    full_name: str
    username: str
    telegram_id: int
