from sqlalchemy import Column, Integer, String, Numeric, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products_product'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(50), nullable=False)
    photo = Column(String(200), nullable=True)
    price = Column(Numeric(precision=200, scale=2), nullable=False)
    description = Column(Text, nullable=False)
    category_code = Column(String(200), nullable=False)
    category_name = Column(String(200), nullable=False)
    subcategory_code = Column(String(34), nullable=False)
    subcategory_name = Column(String(30), nullable=False)


class Users(Base):
    __tablename__ = 'products_users'
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=True)
    username = Column(String(30), unique=True, nullable=True)
    telegram_id = Column(Integer, primary_key=True)
