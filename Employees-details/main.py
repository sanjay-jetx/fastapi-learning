from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Storage
employees = {}

# Model
class Employee(BaseModel):
    id: int
    name: str
    age: int
    salary: int
    department: str


@app.get("/")
def home():
    return {"message": "Employee API Running"}


# Add employee
@app.post("/employee")
def add_employee(emp: Employee):

    if emp.id in employees:
        return {"error": "Employee already exists"}

    employees[emp.id] = emp

    return {"message": "Employee added successfully"}


# View employees
@app.get("/employees")
def get_employees():

    return employees