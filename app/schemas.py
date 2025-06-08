from pydantic import BaseModel

class FlightResponse(BaseModel):
    airline: str
    number: str
    departure_date: str
    status: str
    departure_airport: str
    arrival_airport: str

    class Config:
        orm_mode = True
