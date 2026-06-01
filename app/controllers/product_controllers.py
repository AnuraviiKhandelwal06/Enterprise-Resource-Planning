from app.services.product_services import ProductService


class ProductController:

    def __init__(self):
        self.service = ProductService()

    def add_product_controller(self, product):
        return self.service.add_product_service(product)

    def view_products_controller(self):
        return self.service.view_products_service()

    def search_product_controller(self, item):
        return self.service.search_product_service(item)

    def update_price_controller(self, item, obj):
        return self.service.update_price_service(item, obj)

    def sell_product_controller(self, model):
        return self.service.sell_product_service(model)
    
    def delete_product_controller(self,item_name):
        return self.service.delete_product_service(item_name)
    
    def soft_delete_product_controller(self,item_name):
        return self.service.soft_delete_product_service(item_name)