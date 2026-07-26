import shutil
import subprocess  # nosec B404 - only used with a fixed argument list and shell=False

import requests

PING_BINARY = shutil.which("ping") or "/bin/ping"


def fetch_status_message(url: str) -> str:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return f"{url} responded with {response.status_code}"


def run_healthcheck(host: str) -> str:
    """Ping a host once and return the raw output."""
    result = subprocess.run(  # nosec B603 - fixed argv, host is passed as a single argument
        [PING_BINARY, "-c", "1", host], shell=False, capture_output=True, text=True
    )
    return result.stdout
