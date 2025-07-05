"""
adzuna.py
- Fetches job listings from the Adzuna API
- Uses environment variables for security
"""

import requests
from utils.config_loader import get_env_variable

# Load Adzuna credentials from .env
APP_ID = get_env_variable("ADZUNA_APP_ID")
API_KEY = get_env_variable("ADZUNA_API_KEY")

# Base URL for Adzuna's job search API (UK endpoint)
BASE_URL = "https://api.adzuna.com/v1/api/jobs/gb/search/1"

def fetch_jobs(keyword, results_limit=10):
    """
    Fetch job listings from Adzuna based on the keyword.

    Parameters:
        keyword (str): Search term (e.g., 'python developer')
        results_limit (int): Number of results to fetch (default: 10)

    Returns:
        list: A list of job dictionaries
    """
    params = {
        "app_id": APP_ID,
        "app_key": API_KEY,
        "what": keyword,
        "results_per_page": results_limit,
        "content-type": "application/json"
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise error if request failed
    data = response.json()
    return data.get("results", [])
