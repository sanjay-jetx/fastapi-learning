import sqlite3
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app=FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()

#table creation made here

cursor.execute('''
       create table if not exists items(
            item_id integer primary key ,
            name text not null,
            des text
    )
    ''')

conn.commit()
class item(BaseModel):
    ID:int
    name:str
    des:str


@app.post("/items/create")
def create_items(i:item):
    try:

        # check duplicate
        cursor.execute("select * from items where item_id=? ",(i.ID,))
        existing=cursor.fetchone()

        if existing:
            return{
                "message": "Item already exists",
                "item_id": existing[0]
            }
        cursor.execute("INSERT INTO items (item_id,name, des) VALUES (?,?,?)",(i.ID,i.name,i.des))
        conn.commit()
        return {"message": "Item created successfully",
                "name":i.name,
                "des":i.des}
        
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@app.get("/items/read")
def read_items():
    try:
        cursor.execute("select * from items")
        rows=cursor.fetchall()
        result=[]
        for row in rows:
            result.append({
                "id":row[0],
                "name":row[1],
                "des":row[2]
            })
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

         
     
