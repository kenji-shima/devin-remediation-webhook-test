import requests


def fetch_status_message(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return f"{url} responded with {response.status_code}"
