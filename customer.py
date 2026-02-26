from pydantic import BaseModel , ValidationError , Field

class Address(BaseModel):
    city: str
    pincode: int

class Customer(BaseModel):
    name: str
    address: Address

payload={
    "name":"goftus",
    "address":{
        "city":"chennai",
        "pincode":6001
    }
}

print(Customer(*payload.values()))

print(Customer(**payload))