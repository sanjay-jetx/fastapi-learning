import sqlite3
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app=FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()

#table creation made here

# cursor.execute('''
#        create table if not exists items(
#             item_id integer primary key autoincrement,
#             name text not null,
#             des text
#     )
#     ''')

# conn.commit()
class item(BaseModel):
    name:str
    des:str


@app.post("/items/create")
def create_items(i:item):
    try:
        cursor.execute("INSERT INTO items (name, des) VALUES (?,?)",(i.name, i.des))
        conn.commit()
        return {"message": "Item created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e),detail="Internal Server Error")
     
