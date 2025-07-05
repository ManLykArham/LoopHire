"""
config_loader.py

- Loads environment variables from the .env file
- Provides a helper function to securely access API keys
"""

# Import required libraries
from dotenv import load_dotenv  # To load variables from .env file
import os  # To access system environment variables

# Load all key-value pairs from the .env file into the environment
load_dotenv()

def get_env_variable(key: str) -> str:
    """
    Fetch an environment variable by key.

    Args:
        key (str): The name of the variable.

    Returns:
        str: The value of the variable.

    Raises:
        EnvironmentError: If the variable is not found.
    """
    value = os.getenv(key)  # Try to get the variable
    if value is None:
        raise EnvironmentError(f"Environment variable '{key}' is missing.")
    return value
