from fastapi import APIRouter

from app.models.product_model import (
    AddProduct,
    UpdatePrice,
    SellProduct
)
from app.controllers.product_controllers import (
    ProductController
)
router = APIRouter()
controller = ProductController()

@router.post("/products")
def add_product(product: AddProduct):
    return controller.add_product_controller(product)

@router.get("/products")
def view_products():
    return controller.view_products_controller()

@router.get("/products/{item}")
def search_product(item:str):
    return controller.search_product_controller(item)

@router.put("/products/{item}/price")
def update_price(item:str, obj:UpdatePrice):
    return controller.update_price_controller(item, obj)

@router.put("/products/sell")
def sell_product(model:SellProduct):
    return controller.sell_product_controller(model)

@router.delete("/products/{item_name}")
def delete_product(item_name:str):
    return controller.delete_product_controller(item_name)

@router.put("/products/{item_name}")
def soft_delete_product(item_name:str):
    return controller.soft_delete_product_controller(item_name)