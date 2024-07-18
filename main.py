from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from mylib.logistics import (
    calculate_distance,
    find_coordinates,
    calculate_total_distance,
    calculate_travel_time,
)

app = FastAPI()


class City(BaseModel):
    pass

@app.get("/")
async def root():
    """Home page with GET HTTP method"""
    return {"message": "Hello Logistics INC"}

@app.get()



if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')