from fastapi import FastAPI,Query,HTTPException
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
        raise HTTPException(status_code=400,detail="employee already exist")

    employees[emp.id] = emp

    return {"message": "Employee added successfully"}


# View employees
@app.get("/employees")
def get_employees():

    return employees


@app.get("/employees/{id}")
def get_sparticularid(id:int):
    if id in employees:
        return employees[id]


@app.delete("/employees/{id}")
def delete_sparticularid(id:int = Query(ge=100,le=200 )):
    if id in employees:
        del employees[id]
        return {"message": "Employee deleted successfully"}

    return {"error": "Employee not found"}


@app.put("/employee/{id}")
def update_employee(id:int,emp:employees):
    if emp.id in employees:
        employees[id] = emp
        return {"message": "Employee updated successfully"}
    else:
        return {"error": "Employee not found"}

