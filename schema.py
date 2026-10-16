from pydantic import BaseModel

class Records(BaseModel):
    Temperature:float
    Humidity:float
    Wind_Speed:float
    Cloud_Cover:float
    Pressure:float