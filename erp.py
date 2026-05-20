class Product:
    def __init__(self):
        self.Product = {
            "Laptop": {
                "price": 25000,
                "quantity": 5
            },
            "Monitor": {
                "price": 12000,
                "quantity": 3
            },
            "Headphones": {
                "price": 5000,
                "quantity": 10
            },
            "Speakers": {
                "price": 8000,
                "quantity": 4
            }
        }
    def add_product(self):
        x = input("Enter product you wish to add: ")
        p = int(input("Enter the price: "))
        c = int(input("Enter the quantity: "))
        if p<0:
            print("Price cannot be negative.")
            return
        if c<0:
            print("Quantity should be positive.")
            return
        if x in self.Product:
            self.Product[x]["quantity"] += c
            print("Product already exists.")
            print("Quantity updated successfully!")
            return
        self.Product[x] = {
        "price": p,
        "quantity": c
        }
        print("Product added successfully!!!")
        
    def view_product(self):
        for name, details in self.Product.items():
            print(f"{name} | Price = {details['price']} | Quantity = {details['quantity']}")   
            
    def search_product(self):
        item = input("Enter the item you want to search: ")
        if item in self.Product.keys():
            print(f"{item} | Price = {self.Product[item]['price']} | Quantity = {self.Product[item]['quantity']}")        
        else:
            print(f"{item} is out of stock!!")    
            
    def update_price(self):
        item = input("Enter product name: ")
        if item in self.Product:
            new_price = int(input("Enter new price: "))
            if new_price < 0:
                print("Price cannot be negative.")
                return
            self.Product[item]["price"] = new_price
            print("Price updated successfully!")
        else:
            print("Product not found.")        
                
    def sell_product(self):
        item = input("Enter the item you want to sell: ")
        if item not in self.Product:
            print(f"{item} is not in stock!!")
            return
        quantity = int(input("Enter quantity to sell: "))
        if quantity <= 0:
            print("Quantity should be greater than 0.")
            return
        available_quantity = self.Product[item]["quantity"]
        if quantity > available_quantity:
            print(f"Only {available_quantity} items available in stock.")
            return
        selling_price = int(input("Enter selling price per item: "))
        if selling_price < 0:
            print("Selling price should be greater than 0.")
            return
        total_amount = quantity * selling_price
        self.Product[item]["quantity"] -= quantity
        print(f"{quantity} {item}(s) sold successfully!")
        print(f"Total amount = {total_amount}")
        if self.Product[item]["quantity"] == 0:
            print(f"{item} is now out of stock!")
            
p1 = Product()
while True:
    print("\n1) Add Product")
    print("2) View Product")
    print("3) Search Product")
    print("4) Update Price")
    print("5) Sell Product")
    print("6) Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            p1.add_product()
        case 2:
            p1.view_product()
        case 3:
            p1.search_product()
        case 4:
            p1.update_price()
        case 5:
            p1.sell_product()
        case 6:
            print("Goodbye!")
            break
        case _:
            print("Invalid choice! Please enter between 1 and 6.") 