from app.database.database import products


class ProductRepository:

    def get_all_products(self):
        return products

    def get_single_product(self, item):
        return products.get(item)

    def add_product_repo(self, product):

        products[product.name] = {
            "price": product.price,
            "quantity": product.quantity
        }

    def update_quantity_repo(self, item, quantity):

        products[item]["quantity"] += quantity

    def update_price_repo(self, item, price):

        products[item]["price"] = price

    def reduce_quantity_repo(self, item, quantity):

        products[item]["quantity"] -= quantity