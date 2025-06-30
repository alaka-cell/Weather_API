from fastapi import FastAPI
from pydantic import BaseModel
from tools.weather_tool import get_weather
import os

app = FastAPI()

class Input(BaseModel):
    input: str

@app.post("/tools/weather")
async def weather_endpoint(data: Input):
    city = data.input
    result = get_weather(city)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
