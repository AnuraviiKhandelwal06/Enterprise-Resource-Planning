from fastapi import HTTPException
from app.repository.product_repository import ProductRepository


class ProductService:

    def __init__(self):

        self.repo = ProductRepository()

    def add_product_service(self, product):

        if product.price < 0:
            raise HTTPException(
                status_code=400,
                detail="Price cannot be negative."
            )

        if product.quantity < 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity should be positive."
            )

        existing_product = self.repo.get_single_product(product.name)

        if existing_product:

            self.repo.update_quantity_repo(
                product.name,
                product.quantity
            )

            return {
                "message":
                    "Product found. Quantity updated successfully!!"
            }

        self.repo.add_product_repo(product)

        return {
            "message": "Product added successfully!!"
        }

    def view_products_service(self):

        return self.repo.get_all_products()

    def search_product_service(self, item):

        product = self.repo.get_single_product(item)

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"{item} not found"
            )

        return product

    def update_price_service(self, item, obj):

        product = self.repo.get_single_product(item)

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Item not found."
            )

        if obj.price < 0:
            raise HTTPException(
                status_code=400,
                detail="Price should be positive."
            )

        self.repo.update_price_repo(item, obj.price)

        return {
            "message": "Price updated successfully!!"
        }

    def sell_product_service(self, model):

        product = self.repo.get_single_product(
            model.item_name
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"{model.item_name} out of stock!!"
            )

        if model.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity should be positive."
            )

        if model.selling_price < 0:
            raise HTTPException(
                status_code=400,
                detail="Selling price should be positive."
            )

        available_quantity = product["quantity"]

        if model.quantity > available_quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Only {available_quantity} items available."
            )

        total_amount = (
            model.quantity *
            model.selling_price
        )

        self.repo.reduce_quantity_repo(
            model.item_name,
            model.quantity
        )

        return {
            "items_sold": model.quantity,
            "total_amount": total_amount,
            "remaining_quantity":
                product["quantity"]
        }