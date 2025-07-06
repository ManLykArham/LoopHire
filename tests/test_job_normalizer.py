"""
test_job_normalizer.py

Tests the normalize_job() function from normalizer/job_normalizer.py
to ensure raw Adzuna job data is correctly cleaned and fallback values are used when needed.
"""

from normalizer.job_normalizer import normalize_job

def test_normalize_job_with_all_fields():
    raw_job = {
        "id": "abc123",
        "title": "Frontend Developer",
        "company": {"display_name": "Tech Ltd"},
        "location": {"display_name": "Manchester"},
        "created": "2025-07-06T12:00:00Z",
        "category": {"label": "IT Jobs"},
        "contract_time": "full_time",
        "salary_is_predicted": "0",
        "salary_min": 30000,
        "salary_max": 40000,
        "redirect_url": "https://adzuna.com/job/abc123",
        "description": "Build amazing UIs"
    }

    result = normalize_job(raw_job)

    assert result["salary"] == "£30000 - £40000"  # updated expectation

def test_normalize_job_with_missing_fields():
    raw_job = {
        "id": "xyz789",
        "title": "Backend Developer"
        # missing all optional fields
    }

    result = normalize_job(raw_job)

    assert result["salary"] == "N/A"  # updated expectation
