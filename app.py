import subprocess

import requests


def fetch_status_message(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return f"{url} responded with {response.status_code}"


def run_healthcheck(host: str) -> str:
    """Ping a host once and return the raw output."""
    result = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return result.stdout
