from sqlalchemy import text
from app.database.connection_db import engine


class ProductRepository:

    def get_all_products(self):
        with engine.connect() as conn:
            result = conn.execute(
                text("SELECT * FROM inventory")
            )
            return [
                dict(row._mapping)
                for row in result
            ]


    def get_single_product(self, product_name):
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT *
                    FROM inventory
                    WHERE product_name = :product_name
                """),
                {"product_name": product_name}
            )
            product = result.fetchone()
            if product:
                return dict(product._mapping)
            return None

    
    def add_product_repo(self, product):
        with engine.connect() as conn:
            conn.execute(
                text("""
                    INSERT INTO inventory
                    (
                        product_name,
                        price,
                        quantity
                    )

                    VALUES
                    (
                        :product_name,
                        :price,
                        :quantity
                    )
                """),
                {
                    "product_name": product.name,
                    "price": product.price,
                    "quantity": product.quantity
                }
            )
            conn.commit()

    
    def update_price_repo(self, item, new_price):
        with engine.connect() as conn:
            conn.execute(
                text("""
                    UPDATE inventory
                    SET price = :price
                    WHERE product_name = :item
                """),
                {
                    "price": new_price,
                    "item": item
                }
            )
            conn.commit()


    def sell_product_repo(
        self,
        product_name,
        quantity,
        selling_price
    ):
        with engine.connect() as conn:
            result = conn.execute(
                text("""
                    SELECT *
                    FROM inventory
                    WHERE product_name = :product_name
                """),
                {"product_name": product_name}
            )
            product = result.fetchone()
            if not product:
                return {
                    "message": "Product not found"
                }
            product_data = dict(product._mapping)
            available_quantity = (
                product_data["quantity"]
            )
            if quantity > available_quantity:

                return {
                    "message":
                        f"Only {available_quantity} items available"
                }
            conn.execute(
                text("""
                    UPDATE inventory
                    SET quantity = quantity - :quantity
                    WHERE product_name = :product_name
                """),
                {
                    "quantity": quantity,
                    "product_name": product_name
                }
            )
            total_amount = (
                quantity * selling_price
            )
            conn.execute(
                text("""
                    INSERT INTO sales
                    (
                        product_id,
                        quantity_sold,
                        selling_price,
                        total_amount
                    )
                    VALUES
                    (
                        :product_id,
                        :quantity_sold,
                        :selling_price,
                        :total_amount
                    )
                """),
                {
                    "product_id":    product_data["product_id"],
                    "quantity_sold": quantity,
                    "selling_price":    selling_price,
                    "total_amount":  total_amount
                }
            )

            conn.commit()
            return {
                "message": "Product sold successfully",
                "total_amount":  total_amount
            }