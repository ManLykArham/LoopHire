"""
tests/test_adzuna.py

- Tests the fetch_jobs() function from adzuna.py
- Mocks the Adzuna API response to avoid real network calls
"""

import responses  # For mocking HTTP requests
from api_clients.adzuna import fetch_jobs, BASE_URL

@responses.activate
def test_fetch_jobs_with_mocked_response():
    # Arrange: Define fake response data
    fake_jobs = [
        {
            "id": "abc123",
            "title": "Python Developer",
            "company": {"display_name": "Tech Co"},
            "location": {"display_name": "London"},
            "created": "2025-07-06T10:00:00Z",
            "category": {"label": "IT Jobs"},
            "contract_time": "full_time",
            "salary_is_predicted": "0",
            "salary_min": 30000,
            "salary_max": 40000,
            "redirect_url": "https://adzuna.com/job/abc123",
            "description": "Exciting role"
        }
    ]

    # Set up mock response
    responses.add(
        responses.GET,
        BASE_URL,
        json={"results": fake_jobs},
        status=200
    )

    # Act: Call fetch_jobs
    results = fetch_jobs("python")

    # Assert: Check we received expected mocked data
    assert isinstance(results, list)
    assert len(results) == 1
    assert results[0]["id"] == "abc123"
    assert results[0]["title"] == "Python Developer"
