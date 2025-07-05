"""
main.py
-------------
Fetches job listings from the Adzuna API and saves them to a local JSON file.
"""

from api_clients.adzuna import fetch_jobs
from utils.file_saver import save_jobs
from normalizer.job_normalizer import normalize_job
from models.job import Job

# Define multiple search queries
search_queries = [
    "graduate software engineer",
    "junior backend developer",
    "entry level frontend engineer"
]

all_jobs: list[Job] = []

# Loop through queries and fetch + normalize jobs
for query in search_queries:
    print(f"\n Fetching jobs for: '{query}'")
    raw_jobs = fetch_jobs(query, results_limit=1)

    if not raw_jobs:
        print(f" No jobs found for: '{query}'")
        continue

    for raw_job in raw_jobs:
        # Normalize the raw API job
        job_data = normalize_job(raw_job)

        # Convert normalized job into Job object
        job = Job(**job_data)
        all_jobs.append(job)

        # Display formatted job info
        print(f"""
        Job Title: {job.title}
        Company: {job.company}
        Location: {job.location}
        Posted: {job.created}
        Category: {job.category}
        Contract: {job.contract}
        Salary: {job.salary}
        Apply Here: {job.url}
        Description: 
        {job.description}
        {'=' * 80}
        """)

# Save all Job objects
save_jobs(all_jobs)
