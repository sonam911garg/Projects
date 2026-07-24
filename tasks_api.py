from fastapi import FastAPI
import json
from pydantic import BaseModel

class Name(BaseModel):
    name: str
    number: int

app = FastAPI()

@app.get("/")
def home():
    return ({"message": "home"})

@app.get("/name")
def name():
    try:
        with open("home.json", "r") as f:
            y = json.load(f)

    except:
        y = []
    return y

@app.post("/title")
def title(data: Name):
    try:
        with open("home.json", "r") as f:
            y = json.load(f)
    except:
        y = []
    
    y.append({"name": data.name, "number": data.number})
    
    with open("home.json", "w") as f:
        json.dump(y, f)
    
    return {"added": data.name}
        