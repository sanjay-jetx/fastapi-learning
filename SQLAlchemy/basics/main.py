from fastapi import FastAPI
from SQLAlchemy.basics.routers import router

app = FastAPI()

app.include_router(router)