from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

products = []
next_id = 1 

class ProductCreate(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    in_stock: bool = True

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

@app.get("/")
def home():
    return {"message":"Products API active!"}

@app.get("/products", response_model=list[ProductResponse])
def list_products():
    return products

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
        
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    global next_id
    
    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "in_stock": product.in_stock
    }
    
    products.append(new_product)
    next_id += 1
    
    return new_product

@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate):
    for existing_product in products:
        if existing_product["id"] == product_id:
            existing_product["name"] = product.name
            existing_product["price"] ==product.price
            existing_product["in_stock"] = product.in_stock
            
            return existing_product
        
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            deleted_product = products.pop(index)
            return {
                "message": "Produto deletado com sucesso",
                "product": deleted_product
            }

    raise HTTPException(status_code=404, detail="Product not found")
