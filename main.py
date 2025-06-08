from fastapi import FastAPI, Query
from app.scraper import scrape_flight_data
from app.database import SessionLocal, engine
from app import models, crud, schemas

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

@app.get("/api/flight-info", response_model=schemas.FlightResponse)
def get_flight_info(
    airline: str = Query(...),
    number: str = Query(...),
    date: str = Query(...)
):
    db = SessionLocal()
    flight = crud.get_cached_flight(db, airline, number, date)
    if flight:
        return flight
    flight_data = scrape_flight_data(airline, number, date)
    saved_flight = crud.save_flight(db, flight_data)
    return saved_flight
