from fastapi import APIRouter

from app.models.product_model import (
    AddProduct,
    UpdatePrice,
    SellProduct
)

from app.services.product_services import InventoryService

router = APIRouter()

# OBJECT CREATION
inventory_obj = InventoryService()


@router.post("/products")
def add_product(product: AddProduct):

    return inventory_obj.add_product(product)


@router.get("/products")
def get_products():

    return inventory_obj.view_products()


@router.get("/products/{item}")
def get_single_product(item: str):

    return inventory_obj.search_product(item)


@router.put("/products/{item}/price")
def update_product_price(item: str, obj: UpdatePrice):

    return inventory_obj.update_price(item, obj)


@router.put("/products/sell")
def sell_product(model: SellProduct):

    return inventory_obj.sell_product(model)