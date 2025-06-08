from app.models import Flight
from app.schemas import FlightResponse

def get_cached_flight(db, airline, number, date):
    return db.query(Flight).filter_by(airline=airline, number=number, departure_date=date).first()

def save_flight(db, data):
    flight = Flight(**data)
    db.add(flight)
    db.commit()
    db.refresh(flight)
    return flight
