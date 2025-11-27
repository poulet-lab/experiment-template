"""Core experiment execution logic.

This module contains the main experiment workflow functions that execute
the experimental procedures, collect data, and manage the experiment flow.

Best Practices:
    - Keep experiment logic separate from setup and wrapup
    - Organise experiment into clear phases (training, experimental, etc.)
    - Handle errors gracefully and save progress when possible
    - Log important events and data collection points
    - Use clear function names that describe what each phase does
    - Different sections should generally be written in separate scripts/modules
      that are imported here (e.g., training_staircase.py, experiment_staircase.py)
      rather than implementing everything directly in this file

Structure:
    - experiment(): Main experiment function that orchestrates the workflow
    - Import functions from separate modules for each phase (e.g., from .training import training_phase)

Example Usage:
    ```python
    from .experiment import experiment
    
    experiment(folder_path=Path("data/raw/participant_001"))
    ```
"""

import time
from pathlib import Path

from rich.console import Console

console = Console()


def experiment(folder_path: Path) -> None:
    """Execute the main experiment workflow.
    
    This function contains the core experiment logic. It should be organised
    into clear sections that can be easily understood and modified.
    
    Note: Different sections should generally be written in separate scripts/modules
    that are imported here (e.g., from .training_staircase import training_staircase)
    rather than implementing everything directly in this file. This keeps the code
    modular, testable, and easier to maintain.
    
    Args:
        folder_path: Path to the experiment data folder.
    
    Example:
        ```python
        from .training_staircase import training_staircase
        from .experiment_staircase import experiment_staircase
        
        def experiment(folder_path):
            collect_participant_info(folder_path)
            
            training_staircase(folder_path, ...)
            experiment_staircase(folder_path, ...)
            
            save_experiment_metadata(folder_path)
        ```
    """
    start_time = time.time()
    
    console.print("Starting experiment")
    console.print(f"Data folder: {folder_path}")
    
    try:
        console.print("Collecting participant information...")
        
        console.print("Running training phase...")
        
        console.print("Running experimental phase...")
        
        end_time = time.time()
        duration = end_time - start_time
        
        duration_file = folder_path / "experiment_duration.txt"
        with open(duration_file, "w") as f:
            f.write(f"{duration:.2f} seconds\n")
        
        console.print(f"Experiment completed in {duration:.2f} seconds")
        
    except Exception as e:
        console.print(f"[Error] Experiment failed: {e}", style="red")
        raise

