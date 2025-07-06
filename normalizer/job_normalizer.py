"""
job_normalizer.py
---------------------
Extracts and formats essential job fields from raw Adzuna API data.
"""

from models.job import Job

def normalize_job(raw: dict) -> dict:
    """
    Extracts and normalizes key fields from a raw Adzuna job dictionary.

    Args:
        raw (dict): Raw job data from Adzuna API.

    Returns:
        dict: Normalized job dictionary with consistent structure.
    """
    # Determine salary formatting
    salary_is_predicted = raw.get("salary_is_predicted") == "1"
    salary_min = raw.get("salary_min")
    salary_max = raw.get("salary_max")

    if salary_min is not None and salary_max is not None:
        if salary_is_predicted:
            salary = f"£{salary_max} (predicted)"
        else:
            salary = f"£{salary_min} - £{salary_max}"
    else:
        salary = "N/A"

    return {
        "id": raw.get("id", "N/A"),
        "title": raw.get("title", "N/A"),
        "company": raw.get("company", {}).get("display_name", "N/A"),
        "location": raw.get("location", {}).get("display_name", "N/A"),
        "created": raw.get("created", "N/A"),
        "category": raw.get("category", {}).get("label", "N/A"),
        "contract": raw.get("contract_time", "N/A"),
        "salary": salary,
        "url": raw.get("redirect_url", "N/A"),
        "description": raw.get("description", "N/A"),
    }
