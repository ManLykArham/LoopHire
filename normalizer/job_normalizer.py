"""
job_normalizer.py
---------------------
Extracts and formats essential job fields from raw Adzuna API data.
"""

from models.job import Job

def normalize_job(job: dict) -> dict:
    """
    Converts a raw Adzuna job dictionary into a clean dictionary.

    Args:
        job (dict): Raw job data from Adzuna API

    Returns:
        dict: A dictionary with essential fields only
    """
    return {
        "id": job.get("id", ""),
        "title": job.get("title", "N/A"),
        "company": job.get("company", {}).get("display_name", "N/A"),
        "location": job.get("location", {}).get("display_name", "N/A"),
        "created": job.get("created", "N/A"),
        "category": job.get("category", {}).get("label", "N/A"),
        "contract": job.get("contract_time", "N/A"),
        "salary": f"£{job.get('salary_max', 'N/A')} (predicted)",
        "url": job.get("redirect_url", "N/A"),
        "description": job.get("description", "N/A")
    }
