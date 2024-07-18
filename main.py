from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from mylib.logistics import cities_list

app = FastAPI()


class City(BaseModel):
    name: str


@app.get("/")
async def root():
    """Home page with GET HTTP method"""
    return {"message": "Hello Logistics INC"}


@app.get("/cities")
async def cities():
    """Returns back the List of citiesbthat are avilable to get further information"""
    return {"cities": cities_list()}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
