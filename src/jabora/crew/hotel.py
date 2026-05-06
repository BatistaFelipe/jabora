import requests
from crewai.tools import tool

from ..config import get_env

SERPAPI_URL = "https://serpapi.com/search.json"

@tool("Hotel Search Tool")
def search_hotels(city_code: str, check_in_date: str, check_out_date: str) -> str:
    """
    Searches for hotels in a specific city using SerpApi (Google Hotels).
    Args:
        city_code: Search query (e.g., 'NYC' or 'New York')
        check_in_date: Check-in date in YYYY-MM-DD format
        check_out_date: Check-out date in YYYY-MM-DD format
    """
    api_key = get_env("SERPAPI_API_KEY")

    params = {
        "engine": "google_hotels",
        "q": city_code,
        "check_in_date": check_in_date,
        "check_out_date": check_out_date,
        "api_key": api_key,
        "hl": "en",
        "currency": "USD"
    }
    
    try:
        hotel_res = requests.get(SERPAPI_URL, params=params)
        hotel_res.raise_for_status()
        
        data = hotel_res.json()
        properties = data.get("properties", [])
        
        results = []
        for hotel in properties[:5]:
            name = hotel.get("name", "Unknown")
            price = hotel.get("rate_per_night", {}).get("lowest", "Unknown")
            results.append(f"Hotel: {name} | Price per night: {price}")
            
        return "\n".join(results) if results else "No hotels found."
    except Exception as e:
        return f"API Search Error: {str(e)}"
