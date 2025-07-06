"""
test_file_saver.py

Unit tests for the save_jobs() and load logic in file_saver.py.
- Tests correct saving of job data
- Ensures deduplication and sorting are working
"""

import os
import json
import tempfile
from utils.file_saver import save_jobs
from models.job import Job


def test_save_jobs_deduplicates_and_sorts(monkeypatch):
    # Create a temporary file path (we override the global DATA_PATH to point here)
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        fake_path = tmp.name

    try:
        # Patch DATA_PATH to point to our temp file
        monkeypatch.setattr("utils.file_saver.DATA_PATH", fake_path)

        # Create Job objects (including a duplicate)
        job1 = Job(
            id="1",
            title="Backend Dev",
            company="Tech Co",
            location="Manchester",
            created="2025-07-01",
            category="IT",
            contract="full_time",
            salary="£50,000",
            url="https://example.com/1",
            description="Exciting backend role"
        )

        job2 = Job(
            id="2",
            title="Frontend Dev",
            company="Web Inc",
            location="London",
            created="2025-07-03",  # newer date
            category="IT",
            contract="part_time",
            salary="£45,000",
            url="https://example.com/2",
            description="Frontend position"
        )

        duplicate = Job(
            id="1",  # same as job1
            title="Backend Dev",
            company="Tech Co",
            location="Manchester",
            created="2025-07-01",
            category="IT",
            contract="full_time",
            salary="£50,000",
            url="https://example.com/1",
            description="Exciting backend role"
        )

        # Save jobs (including a duplicate)
        save_jobs([job1, job2, duplicate])

        # Load back from temp file
        with open(fake_path, "r", encoding="utf-8") as f:
            saved = json.load(f)

        # Assert: Only 2 unique jobs
        assert len(saved) == 2

        # Assert: Sorted by 'created' date (job2 should come first)
        assert saved[0]["id"] == "2"
        assert saved[1]["id"] == "1"

    finally:
        # Cleanup: delete temp file
        os.remove(fake_path)
