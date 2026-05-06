import requests
from crewai.tools import tool

from ..config import get_env
SERPAPI_URL = "https://serpapi.com/search.json"

@tool("Flight Search Tool")
def search_flights(origin: str, destination: str, departure_date: str) -> str:
    """
    Searches for flight data using SerpApi (Google Flights).
    Args:
        origin: IATA code (e.g., 'GRU')
        destination: IATA code (e.g., 'JFK')
        departure_date: Date in YYYY-MM-DD format
    """
    api_key = get_env("SERPAPI_API_KEY")

    params = {
        "engine": "google_flights",
        "departure_id": origin,
        "arrival_id": destination,
        "outbound_date": departure_date,
        "type": "2", # 2 indicates one-way flight
        "api_key": api_key,
        "hl": "en"
    }
    
    try:
        flight_res = requests.get(SERPAPI_URL, params=params)
        flight_res.raise_for_status()
        
        data = flight_res.json()
        best_flights = data.get("best_flights", [])
        
        results = []
        for flight in best_flights[:3]:
            price = flight.get("price", "Unknown")
            flights_info = flight.get("flights", [])
            airline = flights_info[0].get("airline", "Unknown") if flights_info else "Unknown"
            results.append(f"Airline: {airline} | Price: {price}")
            
        return "\n".join(results) if results else "No flights found."
    except Exception as e:
        return f"API Search Error: {str(e)}"
