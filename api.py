import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_data(name):
    url = f"{BASE_URL}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


