"""Centralised experimental parameters and constants.

This module serves as the single source of truth for all experimental variables.
By centralising parameters here, we ensure consistency across the experiment
and enable easy tracking of what parameters were used in each session.

Best Practices:
    - All experimental parameters should be defined here, not scattered across modules
    - Use UPPERCASE naming for all constants (following software engineering best practices)
    - Keep parameters immutable - do not modify them during runtime
    - During setup, this file is copied to the experiment data folder for reproducibility
    - Group related parameters together with clear section organisation

Example Usage:
    ```python
    from .globals import BASE_PATH, EXAMPLE_DEVICE_PORT, EXAMPLE_BASELINE_VALUE
    
    data_folder = BASE_PATH / "data" / "raw"
    device = initialise_device(EXAMPLE_DEVICE_PORT)
    set_value(EXAMPLE_BASELINE_VALUE)
    ```

Reproducibility:
    The setup.py module automatically copies this file to the experiment data folder
    as 'copy_globals.py', allowing you to track exactly which parameters were used
    for each experimental session.
"""
from pathlib import Path
# Paths
EXAMPLE_PATH = "Users/username/Documents/data/raw"
EXAMPLE_RAW_PATH = Path(EXAMPLE_PATH) / "raw"
EXAMPLE_PROCESSED_PATH = Path(EXAMPLE_PATH) / "processed"
EXAMPLE_ANALYZED_PATH = Path(EXAMPLE_PATH) / "analyzed"
EXAMPLE_EXTERNAL_PATH = Path(EXAMPLE_PATH) / "external"
EXAMPLE_OTHER_PATH = Path(EXAMPLE_PATH) / "other"

# Variables DEVICE 1 (example)
EXAMPLE_DEVICE_1_STRING = 'example_value'
EXAMPLE_DEVICE_1_FLOAT = 32.5
EXAMPLE_DEVICE_1_INTEGER = 45
EXAMPLE_DEVICE_1_BOOLEAN = True

# Variables DEVICE 2 (example)
EXAMPLE_DEVICE_2_STRING = 'example_value'
EXAMPLE_DICTIONARY = {'key1': 'value1', 'key2': 42}
EXAMPLE_LIST = [1, 2, 3, 4, 5]
EXAMPLE_NONE = None