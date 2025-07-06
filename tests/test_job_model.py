"""
test_job_model.py
-------------------
Unit tests for the Job data model (Job class in models/job.py).
"""

# Import the Job class from the models module
from models.job import Job

# Define a test function to verify the Job class's to_dict and from_dict methods
def test_job_to_dict_and_from_dict():
    # Create a Job object with sample data
    job = Job(
        id="123",
        title="Software Engineer",
        company="Tech Co",
        location="London",
        created="2025-07-06T00:00:00Z",
        category="Engineering",
        contract="full_time",
        salary="£40000",
        url="https://example.com/job/123",
        description="Great opportunity"
    )

    # Convert to dictionary and back
    job_dict = job.to_dict()
    recreated_job = Job.from_dict(job_dict)

    # Check all fields match
    assert recreated_job.id == job.id
    assert recreated_job.title == job.title
    assert recreated_job.company == job.company
    assert recreated_job.location == job.location
    assert recreated_job.created == job.created
    assert recreated_job.category == job.category
    assert recreated_job.contract == job.contract
    assert recreated_job.salary == job.salary
    assert recreated_job.url == job.url
    assert recreated_job.description == job.description
