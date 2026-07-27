from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "hello"}

@app.post("/user")
def User(create: Item):
    return {"message": "Hello " + create.name}
