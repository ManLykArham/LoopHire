## 2025-07-05

**What I did today:**
- Created `.env` file and loaded secrets using `dotenv`
- Successfully tested Adzuna API with a real key and printed raw job data
- Created `main.py` with clean formatting for job listings
- Built a JSON-saving system (`file_saver.py`) that:
  - Prepends new jobs to maintain newest-first order
  - Deduplicates by job ID
  - Sorts by date
- Built `job_normalizer.py` to extract only essential fields from raw API response
- Introduced support for handling multiple search queries at once
- Ensured JSON uses `indent=4`, UTF-8 encoding, and handles empty files gracefully

**What I learned:**
- How to safely read/write JSON in Python
- How to guard against missing or malformed fields in real-world APIs
- How to handle edge cases like empty files or missing keys
- How to build a modular, reusable project structure in Python
- Learned how virtual environments differ on Windows vs. Linux/macOS
- Practiced: `where python`, `python -m venv venv`, `python -m pip install ...`

**What issues I faced:**
- Crash when reading from an empty JSON file — fixed by adding a fallback to `[]`
- `KeyError` when printing normalized fields — solved by using `.get()` defaults
- API sometimes returns `None` or inconsistent formats — solved with safe access
- Struggled to activate Python venv due to system defaulting to MSYS2
- Fixed it by using the full path to `python.exe` 3.13
- Adjusted PowerShell execution policy with:  
  `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`

**Next goals:**
- Add unit tests for `fetch_jobs()`, `normalize_job()`, and `save_jobs()`
- Add command-line support for dynamic search terms

============================================================================================

## 2025-07-06

**What I did today:**
- Set up `pytest` and added test support for:
  - `Job` model conversion (`to_dict` and `from_dict`)
  - `get_env_variable()` config loader with `monkeypatch`
  - `normalize_job()` with all and missing fields
  - `save_jobs()` with deduplication, sorting, and file I/O mocking
  - `fetch_jobs()` from Adzuna using `responses` to mock HTTP
- Achieved 100% test coverage on:
  - `job.py`
  - `config_loader.py`
  - `file_saver.py`
  - `job_normalizer.py`
- Created `tests/` directory and used `conftest.py` for shared fixtures
- Used `PYTHONPATH=.` trick to resolve `ModuleNotFoundError` on Windows
- Tagged commit `v0.1.1` after finishing core logic

**What I learned:**
- How to write unit tests using `pytest`, `pytest-mock`, and `responses`
- The difference between unit tests and integration tests
- Mocking file reads/writes and HTTP requests for safe test isolation
- Using coverage reports to find untested files
- How to tag versions in Git using `git tag vX.Y.Z && git push origin --tags`

**What issues I faced:**
- `ModuleNotFoundError` when importing modules — fixed by adding `PYTHONPATH=.` in test runner
- API keys not loading properly in test — fixed by `monkeypatch.setenv()`
- Unexpected salary output due to logic in `normalize_job` — fixed by updating test expectations
- Confusion between generic test structure vs. API-specific logic

**Next goals:**
- Add command-line argument support for search terms in `main.py`
- Allow user to type `python main.py "python developer"` for custom queries
- Start planning reusable API structure if more APIs are added later
