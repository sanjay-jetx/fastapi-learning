# from fastapi import FastAPI,Form


# app=FastAPI()

# @app.post("/feedback")
# def feed(name:str = Form(...),
#          email:str = Form(...),
#          number:int=Form(...)):
#     return {
#         "name":name,
#         "email":email,
#         "number":number
#     }


# from fastapi import FastAPI, Form, Depends
# from pydantic import BaseModel

# app = FastAPI()

# # Model
# class LoginForm(BaseModel):
#     username: str
#     password: str

#     # classmethod to handle form input
#     @classmethod
#     def as_form(
#         cls,
#         username: str = Form(...),
#         password: str = Form(...)
#     ):
#         return cls(username=username, password=password)


# # API
# @app.post("/login")
# def login(user: LoginForm = Depends(LoginForm.as_form)):
#     return {
#         "message": "Login successful",
#         "user": user
#     }



from fastapi import FastAPI,Form,Depends
from pydantic import BaseModel

app=FastAPI()

class LoginForm(BaseModel):
    Email:str
    Password:str
    Number:int
    
    @classmethod
    def LoginForm_Details(cls,Email:str=Form(...),Password:str=Form(...),Number:int=Form(...)):
        return cls(Email= Email,Password=Password, Number=Number)
    
@app.post("/login")
def login(inputs:LoginForm=Depends(LoginForm.LoginForm_Details)):
    return {
        "message": "Login successful",
        "Full_details":inputs
    }