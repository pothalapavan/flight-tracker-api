from sqlalchemy import Column, String, Integer, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    airline = Column(String)
    number = Column(String)
    departure_date = Column(String)
    status = Column(String)
    departure_airport = Column(String)
    arrival_airport = Column(String)
