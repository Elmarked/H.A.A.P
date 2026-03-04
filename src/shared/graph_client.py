import requests
from .auth import get_token

GRAPH_BASE = "https://graph.microsoft.com/v1.0"

def graph_get(endpoint):
    token = get_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(f"{GRAPH_BASE}{endpoint}", headers=headers)
    response.raise_for_status()
    return response.json()
