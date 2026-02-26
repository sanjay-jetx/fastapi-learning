from fastapi import FastAPI
from products import Product 
app = FastAPI()


def greet():
    return {"hiii Pranesh"}

@app.get("/")
def gg():
    msg1= greet()
    return msg1 , "hiiii" 


product=Product(id=101,name="sanjay")

@app.get("/product")
def get_all():
    return product
 