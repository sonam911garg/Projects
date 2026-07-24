from fastapi import FastAPI
from pydantic import BaseModel
import json

class Name(BaseModel):
    name: str

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Hello world"}

@app.get("/items")
def item():
    return["item1", "item2", "item3"]

@app.post("/name")
def name1(name1: Name):
    y = []
    y.append(name1.name)
    with open("name.json", "w") as f:
        json.dump(y,f)
    return{"name": name1.name}