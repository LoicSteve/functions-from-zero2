from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from mylib.logistics import (
    cities_list,
    calculate_distance,
    find_coordinates,
    calculate_travel_time,
)

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


# build a post method to calculate the distance between two cities
@app.post("/distance")
async def calculate_distance_post(city1: City, city2: City):
    """Calculate the distance between two cities"""
    return {
        "city1": city1.name,
        "city2": city2.name,
        "distance": calculate_distance(city1.name, city2.name),
    }


# build a post method to calculate the travel time between two cities
@app.post("/travel_time")
async def calculate_travel_time_post(city1: City, city2: City, speed: int = 60):
    """Calculate the travel time between two cities"""
    return {
        "city1": city1.name,
        "city2": city2.name,
        "speed": speed,
        "travel_time": calculate_travel_time(city1.name, city2.name, speed),
    }


# build a post method to find the coordinates of a city
@app.post("/coordinates")
async def find_coordinates_post(city: City):
    """Find the coordinates of a city"""
    return {
        "city": city.name,
        "coordinates": find_coordinates(city.name),
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
