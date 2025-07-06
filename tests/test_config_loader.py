"""
test_config_loader.py

Tests the get_env_variable function in config_loader.py.
Ensures environment variables are loaded correctly and missing keys raise errors.
"""

import pytest
from utils.config_loader import get_env_variable

def test_get_env_variable_success(monkeypatch):
    # Set fake environment variable
    monkeypatch.setenv("ADZUNA_APP_ID", "test_id_123")

    # Test if get_env_variable returns the correct value
    value = get_env_variable("ADZUNA_APP_ID")
    assert value == "test_id_123"

def test_get_env_variable_missing(monkeypatch):
    # Ensure the variable does not exist
    monkeypatch.delenv("FAKE_KEY", raising=False)

    # Test if EnvironmentError is raised for missing key
    with pytest.raises(EnvironmentError):
        get_env_variable("FAKE_KEY")
