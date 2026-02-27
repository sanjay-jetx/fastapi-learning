from fastapi import FastAPI
from products import Product 
app = FastAPI()


def greet():
    return {"hiii Pranesh"}

@app.get("/")
def gg():
    msg1= greet()
    return msg1 , "hiiii" 

#we can create differnt obj for these values
# product1 = Product(id=101, name="sanjay")

# product2 = Product(id=102, name="pranesh")

# product3 = Product(id=103, name="kumar")

#we create the dict for these products
products = [
    Product(
        id=101,
        name="Laptop",
        price=55000.0,
        quantity=5,
        description="Gaming Laptop",
        in_stock=True
    ),
    Product(
        id=102,
        name="Mobile",
        price=20000.0,
        quantity=10,
        description="Android Mobile",
        in_stock=True
    ),

    Product(
        id=103,
        name="Headphone",
        price=1500.0,
        quantity=0,
        description="Wireless Headphone",
        in_stock=False
    )

]



#we get all the product
@app.get("/product")
def get_all():
    return products




#http://127.0.0.1:8000/products?id=101
@app.get("/productss")
def get_product_by_id(id:int):

    for p in products:

        if p.id == id:
            return p

    return {"error": "Product not found"}


#http://127.0.0.1:8000/products
@app.get("/products")
def get_product_by_id():
    return products[0]


@app.get("/product/{id}")
def get_product_by_id(id: int):

    if id > 0 and id <= len(products):
        return products[id-1]

    return {"error": "Product not found"}


@app.post("/product/")
def add_product(new_product:Product):
    products.append(new_product)
    return new_product

@app.put("/product/{id}")
def update_product(id: int, new_product: Product):

    for i in range(len(products)):

        if products[i].id == id:

            products[i] = new_product

            return {"message": "Product updated successfully", "product": new_product}

    return {"error": "Product not found"}


@app.delete("/product")
def delete(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
        
    return "products didnot found"