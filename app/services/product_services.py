from fastapi import HTTPException
from app.database.database import products


class InventoryService:

    def add_product(self, product):

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

        if product.name in products:

            products[product.name]["quantity"] += product.quantity

            return {
                "message": "Quantity updated successfully!!"
            }

        products[product.name] = {
            "price": product.price,
            "quantity": product.quantity
        }

        return {
            "message": "Product added successfully!!"
        }

    def view_products(self):
        return products

    def search_product(self, item):

        if item not in products:
            raise HTTPException(
                status_code=404,
                detail=f"{item} not found"
            )

        return products[item]

    def update_price(self, item, obj):

        if item not in products:
            raise HTTPException(
                status_code=404,
                detail="Item not found."
            )

        if obj.price < 0:
            raise HTTPException(
                status_code=400,
                detail="Price should be positive."
            )

        products[item]["price"] = obj.price

        return {
            "message": "Price updated successfully!!"
        }

    def sell_product(self, model):

        if model.item_name not in products:
            raise HTTPException(
                status_code=404,
                detail="Item out of stock!!"
            )

        if model.quantity <= 0:
            raise HTTPException(
                status_code=400,
                detail="Quantity should be positive."
            )

        available_quantity = products[model.item_name]["quantity"]

        if model.quantity > available_quantity:
            raise HTTPException(
                status_code=400,
                detail=f"Only {available_quantity} items available."
            )

        total_amount = model.quantity * model.selling_price

        products[model.item_name]["quantity"] -= model.quantity

        return {
            "items_sold": model.quantity,
            "total_amount": total_amount,
            "remaining_quantity":
                products[model.item_name]["quantity"]
        }