from fastapi import FastAPI
import asyncio

app=FastAPI()

async def db_call():
    await asyncio.sleep(2)
    return {"data":"fetched"}

@app.get("/data")
async def get_data():
    result = await db_call()
    return result


