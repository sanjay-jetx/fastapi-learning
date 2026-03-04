from pydantic import BaseModel , Field

class Product(BaseModel):
    id: int
    name: str = Field(min_length=3,max_length=15,pattern="^[a-z A-Z]")
    price: float
    quantity: int
    description: str
    in_stock: bool
