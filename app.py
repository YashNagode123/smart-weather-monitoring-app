import os
import requests
import time

def fetch_weather(city_name, api_key):
    """
    Fetches weather data with network error handling and timeout configurations.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    
    start_time = time.time()
    try:
        # Enforcing a 5-second network timeout to handle dropped packets/latency
        response = requests.get(base_url, params=params, timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)
        
        # HTTP Status Code Checks
        if response.status_code == 200:
            data = response.json()
            print(f"[STATUS 200 OK] Response received in {latency}ms")
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "status": data["weather"][0]["description"],
                "latency_ms": latency
            }
        elif response.status_code == 404:
            print(f"[ERROR 404] City '{city_name}' not found.")
        elif response.status_code == 401:
            print("[ERROR 401] Unauthorized API Key.")
        else:
            print(f"[ERROR {response.status_code}] Network query returned non-200 state.")
            
    except requests.exceptions.Timeout:
        print("[NETWORK ERROR] Request timed out. Checking gateway/DNS reachability.")
    except requests.exceptions.ConnectionError:
        print("[NETWORK ERROR] Connection refused or DNS resolution failed.")
    except requests.exceptions.RequestException as e:
        print(f"[FATAL EXCEPTION] Network pipeline error: {e}")
        
    return None

if __name__ == "__main__":
    print("--- Smart Weather Monitoring Service ---")
    mock_api_key = os.getenv("WEATHER_API_KEY", "DEMO_KEY")
    result = fetch_weather("Nashik", mock_api_key)
