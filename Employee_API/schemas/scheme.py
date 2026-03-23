from pydantic import BaseModel,Field;

class Employee(BaseModel):
    emp_id:int
    name:str = Field(...,min_length=2,max_length=50)
    age:int = Field(...,gt=18)
    role:str
    salary:float = Field(..., gt=0)