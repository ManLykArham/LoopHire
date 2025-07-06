# conftest.py
# -------------------------
# This file configures the test environment for pytest.
# It ensures that the root directory of the project (LoopHire/)
# is added to Python’s module search path so that modules like
# 'models.job', 'utils.file_saver', etc., can be imported
# directly in test files without causing ModuleNotFoundError.

import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
