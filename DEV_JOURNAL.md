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
