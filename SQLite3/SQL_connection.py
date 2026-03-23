import sqlite3
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app=FastAPI()

conn=sqlite3.connect("test.db",check_same_thread=False)
cursor=conn.cursor()

#table creation made here

cursor.execute('''
       create table if not exists Employee(
            emp_id integer primary key ,
            Name text not null,
            Age int no null,
            role text,
            salary Real
    )
    ''')

conn.commit()


class item(BaseModel):
    emp_id:int
    Name:str
    Age:int
    role:str
    salary:int


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

         
     
@app.get("/item/readone/{name}")
def read_one(name: str):
    try:
        cursor.execute("select * from items where name = ?", (name,))
        row = cursor.fetchone()

        if row is None:
            raise HTTPException(status_code=404, detail="Item not found")

        return {
            "id": row[0],
            "name": row[1],
            "des": row[2]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.put("/item/update/{item_id}")
def update_item(item_id: int, i: item):
    try:
        cursor.execute(
            "update items set name=?, des=? where item_id=?",
            (i.name, i.des, item_id)
        )
        conn.commit()

        return {"message": "Updated successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.delete("/items/delete/{name}")
def delete(name:str):
    cursor.execute("delete from items where name = ?",(name,))
    conn.commit()