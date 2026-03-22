from fastapi import FastAPI,HTTPException,Cookie,Response
import uuid

app = FastAPI()

name="sanjay"
password="1234"

session={}


@app.post("/session")
def login(ename:str , epass:str , res:Response):
  if name == ename and password==epass:
    sid=str(uuid.uuid4())
    session[sid]={"username":name}
    res.set_cookie(key="sid",value=sid,httponly=True)
    

  else:
    raise HTTPException(status_code=401,detail="invalid credentail")
  