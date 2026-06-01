from fastapi import HTTPException
from app.repository.product_repository import ProductRepository


class ProductService:

    def __init__(self):
        self.repo = ProductRepository()

    def add_product_service(self, product):
        if product.price < 0:
            raise HTTPException(400, "Price cannot be negative")
        if product.quantity < 0:
            raise HTTPException(400, "Quantity should be positive")

        existing_product = self.repo.search_product_repo(product.name)
        if existing_product:
            self.repo.update_quantity_repo(
            product.name,
            product.quantity
            )
            return {
            "message": "Product found. Quantity updated successfully!!"
            }

        self.repo.add_product_repo(product)
        return {
        "message": "Product added successfully!!"
        }

    def view_products_service(self):

        return self.repo.view_product_repo()

    def search_product_service(self, item):

        product = self.repo.search_product_repo(item)

        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"{item} not found"
            )

        return product

    def update_price_service(self, item, obj):
        product = self.repo.search_product_repo(item)

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

        result = self.repo.update_price_repo(item, obj.price)
        return {
        "message": "Price updated successfully!!"
         }

    def sell_product_service(self, model):
        if model.quantity <= 0:
            raise HTTPException(400, "Quantity should be positive")
        if model.selling_price < 0:
            raise HTTPException(400, "Selling price should be positive")
        
        result = self.repo.sell_product_repo(model)
        
        if result.get("message") == "Product not found":
           raise HTTPException(404, "Product not found")
       
        return result
    
    def delete_product_service(self, item_name):
        product = self.repo.search_product_repo(item_name)
        if not product:
            raise HTTPException(
               status_code=404,
               detail="Product not found."
        )
        if product.quantity > 0:
            raise HTTPException(
               status_code=400,
               detail="Cannot delete product because item is in stock!!"
        )
        result = self.repo.delete_product_repo(item_name)
        return result
    
    def soft_delete_product_service(self, item_name):
        product = self.repo.search_product_repo(item_name)

        if not product:
            raise HTTPException(
            status_code=404,
            detail="Product not found"
            )

        if product["quantity"] > 0:
            raise HTTPException(
            status_code=400,
            detail="Cannot delete product because stock exists"
            )

        return self.repo.soft_delete_product_repo(item_name)