from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
products = {
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

class AddProduct(BaseModel):
    name : str
    quantity : int
    price : int
    
class UpdatePrice(BaseModel):
    price : int
    
class SellProduct(BaseModel):
    item_name : str
    quantity : int
    selling_price : int
    
@app.post("/products")
def Add_product(product : AddProduct):
    if product.price<0:
        raise HTTPException(
            status_code=400,
            detail= "Price cannot be negative."
        )
    if product.quantity<0:
        raise HTTPException(
            status_code=400,
            detail="Quantity should be poitive."
        )    
    if product.name in product:
        product[product.name]["quantity"] += product.quantity
        
        return{
            "message" : "Product found.Quantity updated successfully!!"
        }    
    product[product.name] = {
        "price" : product.price,
        "quantity" : product.quantity
    }    
    return{
        "message":"Product added!!"
    }
    
@app.get("/products")
def view_product():
    return products

@app.get("/products/{item}")
def search_product(item:str):
    if item not in products:
        raise HTTPException(
            status_code=404,
            detail=f"{item} not found"
        )
    return products[item]    

@app.put("/products/{item}/price")
def update_price(item : str,obj : UpdatePrice):
    if item not in products:
        raise HTTPException(
            status_word=404,
            detail="Item not found."
        )
    if obj.price<0:
        raise HTTPException(
            status_code=400,
            detail="Price should be positive."
        )
    products[item]["price"] = obj.price   
    return{
        "message" : "Price updated successfully!!"
    } 
    
@app.put("/products/sell")
def sell_product( model : SellProduct):
    if model.item_name not in products:
        raise HTTPException(
            status_code=404,
            detail=f"{model.item_name} out of stock!!"
        )    
    if model.quantity<=0:
        raise HTTPException(
            status_code=400,
            detail="Quantity should be positive."
        )    
    if model.selling_price<0:
        raise HTTPException(
            status_code=400,
            detail="Selling price should be greater than zero."
        )    
    available_quantity = products[model.item_name]["quantity"]
    if model.quantity>available_quantity:
        raise HTTPException(
            status_code=400,
            detail=f"Only {available_quantity} items available in stock."
        )    
    total_amount = model.quantity*model.selling_price
    products[model.item_name]["quantity"] -= model.quantity
    return{
        "message" : f"{model.quantity} items sold.",
        "message" : f"Total amount = {total_amount}",
        "message" : f"Remaining quantity = {products[model.item_name]["quantity"]}"
    }