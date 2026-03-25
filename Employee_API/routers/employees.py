from fastapi import HTTPException , APIRouter
from Employee_API.schemas.scheme import Employee;
from Employee_API.database.database import get_db;

routers = APIRouter()

# @routers.post("/employees")                
# @routers.get("/employees")                  
# @routers.get("/employees/{emp_id}")         
# @routers.put("/employees/{emp_id}")        
# @routers.delete("/employees/{emp_id}")   