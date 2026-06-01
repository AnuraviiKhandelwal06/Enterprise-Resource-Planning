from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from app.database.connection_db import engine
from app.models.product_model import SellProduct
from app.models.product_model import AddProduct

class ProductRepository:

    def view_product_repo(self):
        with engine.begin() as conn:
            result = conn.execute(
                text("""SELECT * FROM inventory 
                     WHERE is_deleted = FALSE
                    """)
            )
            return [
                dict(row._mapping)
                for row in result
            ]


    def search_product_repo(self, product_name):
        with engine.begin() as conn:
            result = conn.execute(
                text("""
                    SELECT *
                    FROM inventory
                    WHERE product_name = :product_name AND is_deleted = FALSE
                """),
                {"product_name": product_name}
            )
            product = result.fetchone()
            if product:
                return{
                    "product_id": product.product_id,
                    "product_name": product.product_name,
                    "price": product.price,
                    "quantity": product.quantity
                }
            return None

    
    def add_product_repo(self, obj:AddProduct):
        try:  
            with engine.begin() as conn:
                conn.execute(
                    text("""
                        INSERT INTO inventory(product_name,price,quantity)
                        VALUES
                        (
                         :product_name,
                         :price,
                         :quantity
                        )
                        """),
                    {
                        "product_name": obj.name,
                        "price": obj.price,
                        "quantity": obj.quantity
                    }
                )
        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred",
                "error": str(e)
            }
                
                
    def update_price_repo(self, product_name, price):
        try:
            with engine.begin() as conn:
               conn.execute(
                text("""
                UPDATE inventory
                SET price = :price
                WHERE product_name = :product_name AND is_deleted = FALSE
                """),
                {
                "product_name": product_name,
                "price": price
                }
            )
        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred",
                "error": str(e)
            }       
            

    def sell_product_repo(self, model: SellProduct):
        try:
            with engine.begin() as conn:
                result = conn.execute(
                    text("""
                    SELECT *
                    FROM inventory
                    WHERE product_name = :product_name AND is_deleted = FALSE
                    """),
                    {"product_name": model.item_name}
                )
                product = result.fetchone()
                if not product:
                    return {
                    "message": "Product not found"
                    }
                available_quantity = product.quantity
                if model.quantity > available_quantity:
                    return {
                        "message":
                        f"Only {available_quantity} items available"
                    }
                conn.execute(
                    text("""
                    UPDATE inventory
                    SET quantity = quantity - :quantity
                    WHERE product_name = :product_name AND is_deleted = FALSE
                    """),
                    {
                    "quantity": model.quantity,
                    "product_name": model.item_name
                    }
                )
                total_amount = (
                model.quantity * model.selling_price
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
                    "product_id": product.product_id,
                    "quantity_sold": model.quantity,
                    "selling_price": model.selling_price,
                    "total_amount":  total_amount
                }
                )
                return {
                "message": "Product sold successfully",
                "total_amount":  total_amount
                }
        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred",
                "error": str(e)
            }    
            
            
    def delete_product_repo(self, item_name):
        try:
            with engine.begin() as conn:
                result = conn.execute(
                text("""
                     Select * from inventory
                     where product_name = :product_name AND is_deleted = FALSE
                    """),
                {
                    "product_name" : item_name
                }
                )
                product = result.fetchone()
                if not product:
                    return{
                    "message" : "Item not found!!"
                    }
                available_quantity = product.quantity
                if available_quantity > 0:
                    return{
                    "message" : "Cannot delete the item. Item still in stock!!"
                    }    
                conn.execute(
                text("""
                     DELETE FROM inventory
                     WHERE product_name = :product_name AND is_deleted = FALSE
                    """),
                {
                    "product_name": item_name
                }
                )
                return{
                "message" : "Product deleted successfully!!"
                }
                
        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred",
                "error": str(e)
            }    
                
            
    def soft_delete_product_repo(self, item_name):
        try:
            with engine.begin() as conn:
                result = conn.execute(
                text("""
                   SELECT product_id, product_name, quantity, is_deleted
                   FROM inventory
                   WHERE product_name = :product_name AND is_deleted = FALSE
                """),
                {"product_name": item_name}
                )
                product = result.fetchone()
                if not product:
                   return None

                if product.quantity > 0:
                    return {
                    "status": "blocked",
                    "message": "Cannot delete product because stock exists"
                    }

                conn.execute(
                text("""
                   UPDATE inventory
                   SET is_deleted = TRUE
                   WHERE product_name = :product_name AND is_deleted = FALSE
                """),
                {"product_name": item_name}
                )

                return {
                "status": "success",
                "message": "Product soft deleted successfully"
                }

        except SQLAlchemyError as e:
            raise Exception(f"Database error: {str(e)}")     
            
    def update_quantity_repo(self, product_name, quantity):
        try:
           with engine.begin() as conn:
                conn.execute(
                text("""
                UPDATE inventory
                SET quantity = quantity + :quantity
                WHERE product_name = :product_name AND is_deleted = FALSE
                """),
                {
                "product_name": product_name,
                "quantity": quantity
                }
                )   
        except SQLAlchemyError as e:
            return {
                "message": "Database error occurred",
                "error": str(e)
            }             