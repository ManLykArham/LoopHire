# utils/file_saver.py

import json
import os
from models.job import Job

DATA_PATH = "data/adzuna_jobs.json"

def save_jobs(new_jobs: list[Job]) -> None:
    """
    Saves new job listings to the local JSON file.
    """

    existing_jobs = []

    # Step 1: Load existing jobs from file if it exists
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            try:
                existing_jobs = json.load(file)
            except json.JSONDecodeError:
                existing_jobs = []

    # Step 2: Convert new Job objects to dicts
    new_jobs_dicts = [job.to_dict() for job in new_jobs]

    # Step 3: Merge new jobs at the top
    combined_jobs = new_jobs_dicts + existing_jobs

    # Step 4: De-duplicate
    seen_ids = set()
    unique_jobs = []
    for job in combined_jobs:
        job_id = job.get("id")
        if job_id and job_id not in seen_ids:
            unique_jobs.append(job)
            seen_ids.add(job_id)

    # Step 5: Sort by posted date (newest first)
    unique_jobs.sort(key=lambda job: job.get("created", ""), reverse=True)

    # Step 6: Save to JSON file
    with open(DATA_PATH, "w", encoding="utf-8") as file:
        json.dump(unique_jobs, file, indent=4, ensure_ascii=False)
