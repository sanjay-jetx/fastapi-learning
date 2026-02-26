from fastapi import FastAPI
from Products_to_display.products import Product
app = FastAPI()


def greet():
    return {"hiii Pranesh"}

@app.get("/")
def gg():
    msg1= greet()
    return msg1 , "hiiii" 
product=Product(101,"sanjay")


@app.get("/product")
def get_all():
    return product
 