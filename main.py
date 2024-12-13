from fastapi import FastAPI

from db.engine import init_db
from routers import customers, rooms

app = FastAPI()

DB_FILE = "sqlite:///hotel.db"
 
@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)
 
@app.get("/")
def read_root():
    return "The server is running"
 
app.include_router(customers.router)
app.include_router(rooms.router)