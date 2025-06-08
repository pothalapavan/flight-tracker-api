import requests
from bs4 import BeautifulSoup

def scrape_flight_data(airline, number, date):
    url = f"https://www.flightstats.com/v2/flight-tracker/{airline}/{number}?year={date[:4]}&month={int(date[5:7])}&date={int(date[8:])}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract details from soup (mock data below for demo)
    return {
        "airline": airline,
        "number": number,
        "departure_date": date,
        "status": "On Time",
        "departure_airport": "DEL",
        "arrival_airport": "BOM"
    }
