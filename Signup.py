from pydantic import BaseModel , ValidationError , Field


class Signup(BaseModel):
    UserName : str=Field(min_length=3 , max_length=12)
    Age:int=Field(ge=18,le=60)
    score:float=Field(default=0.0 , ge=0 , le=100)


try:
    print(Signup(UserName="asss" , Age="19"))
except ValidationError as e:
    print(e)

