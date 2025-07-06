# Changelog

## [0.1.0] - 2025-07-05
### Added
- Initial project folder structure
- Virtual environment support
- .env loader utility in `utils/config_loader.py`

### Fixed
- Git push error by pulling remote README with `--rebase`

### Notes
- Learned how Python venv differs on Windows vs. macOS

=================================================================================================

## [0.1.1] - 2025-07-05
### Added
- Implemented `fetch_jobs()` in `api_clients/adzuna.py` with proper API key loading
- Formatted job output for readability in `main.py`
- Created `file_saver.py` for saving jobs with deduplication and ordering
- Introduced `job_normalizer.py` to extract and standardise job fields
- Set up multiple job queries in `main.py` with normalized output
- Ensured JSON output uses UTF-8 encoding and indent=4

### Changed
- JSON save structure now stores normalized fields only
- Adjusted `main.py` to include modular imports and reusable logic

### Fixed
- Crash on first save due to empty file handled with fallback to `[]`

### Notes
- Learned how to structure Python projects with modules
- Implemented clean formatting, error prevention, and job deduplication

=================================================================================================

## [0.2.0] - 2025-07-06
### Added
- Introduced `tests/` folder with pytest-based unit tests
- Test coverage for:
  - Job model serialization (`test_job_model.py`)
  - Config loader (`test_config_loader.py`)
  - Job normalization (`test_job_normalizer.py`)
  - File saving logic (`test_file_saver.py`)
  - Adzuna API fetcher with mocked responses (`test_adzuna.py`)
- Used `responses` to mock Adzuna HTTP responses
- Mocked file I/O and environment variables with `pytest-mock`

### Changed
- Ensured codebase is 100% testable and modular
- Used `PYTHONPATH=.` to resolve import paths during testing

### Notes
- Learned `pytest`, `pytest-cov`, `pytest-mock`, `responses`
- Mastered mocking strategies for environment, network, and file systems
- Maintained 100% coverage on key modules
