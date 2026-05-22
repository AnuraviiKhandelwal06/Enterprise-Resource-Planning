from pydantic import BaseModel


class AddProduct(BaseModel):
    name: str
    quantity: int
    price: int


class UpdatePrice(BaseModel):
    price: int


class SellProduct(BaseModel):
    item_name: str
    quantity: int
    selling_price: int