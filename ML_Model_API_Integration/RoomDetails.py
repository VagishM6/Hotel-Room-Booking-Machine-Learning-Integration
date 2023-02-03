from pydantic import BaseModel


class RoomOccupancy(BaseModel):
    Temperature: float 
    Humidity: float 
    Light: float 
    CO2: float
    HumidityRatio: float