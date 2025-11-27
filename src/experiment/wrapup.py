"""Post-experiment cleanup and finalisation.

This module handles all tasks that should be performed after experiment completion,
including data validation, final data collection, result generation, and cleanup.

Best Practices:
    - Always call wrapup() at the end of the experiment (use try/finally)
    - Validate data completeness and quality before finishing
    - Collect any final measurements or metadata
    - Generate summary plots or reports
    - Copy data to backup locations (cloud, research drive, etc.)
    - Clean up hardware connections and resources
    - Provide clear feedback to the experimenter about completion status

Structure:
    - wrapup(): Main wrapup function that orchestrates all cleanup tasks
    - validate_data_files(): Check that all required data files exist
    - collect_final_metadata(): Gather any remaining experiment information
    - run_sanity_checks(): Automatic code to do sanity checks and summarise results

Example Usage:
    ```python
    from .wrapup import wrapup
    
    try:
        run_experiment()
    finally:
        wrapup(folder_path=Path("data/raw/participant_001"))
    ```
"""

from pathlib import Path
from typing import Dict, List

from rich.console import Console

console = Console()


def validate_data_files(folder_path: Path, required_files: List[str]) -> Dict[str, bool]:
    """Validate that all required data files exist.
    
    This function should check that all necessary data files are present
    in the experiment folder. Return a dictionary mapping filenames to
    their existence status.
    
    Args:
        folder_path: Path to experiment data folder.
        required_files: List of required filenames to check.
    
    Returns:
        Dictionary mapping filenames to existence status (True/False).
    
    Example:
        ```python
        required = ['trials.csv', 'metadata.json', 'copy_globals.py']
        validation = validate_data_files(folder_path, required)
        all_present = all(validation.values())
        ```
    """
    console.print(f"Validating data files in {folder_path}")
    
    results = {}
    for filename in required_files:
        file_path = folder_path / filename
        results[filename] = file_path.exists()
    
    return results


def collect_final_metadata(folder_path: Path) -> None:
    """Collect any final metadata or measurements.
    
    This function should prompt for any remaining information that needs
    to be recorded at the end of the experiment.
    
    Args:
        folder_path: Path to experiment data folder.
    """
    console.rule("[bold cyan]Final Metadata Collection[/]")
    
    console.print(f"Collecting final metadata for {folder_path}")
    
    console.print(
        "Please provide any final information about the experiment session.",
        style="cyan"
    )
    
    input("\nPress Enter to continue...")


def run_sanity_checks(folder_path: Path) -> None:
    """Run automatic sanity checks and summarise results.
    
    This function should perform automatic validation of data quality,
    completeness, and consistency. Use your functions or code to perform
    sanity checks and summarise the results.
    
    Args:
        folder_path: Path to experiment data folder.
    """
    console.rule("[bold cyan]Running Sanity Checks[/]")
    
    console.print(f"Running sanity checks on data in {folder_path}")
    
    console.print("Use your functions or code to perform sanity checks here.")


def backup_data(folder_path: Path) -> None:
    """Back up experiment data to research drive or cloud storage.
    
    This function should copy the experiment data folder to a backup location.
    Use your functions or code to back up your data.
    
    Args:
        folder_path: Path to experiment data folder.
    """
    console.rule("[bold cyan]Backing Up Data[/]")
    
    console.print(f"Copying data from {folder_path}")
    
    console.print("Use your functions or code to back up your data here.")


def wrapup(folder_path: Path) -> None:
    """Handle end-of-experiment wrap-up tasks.
    
    This function orchestrates all post-experiment tasks:
    1. Validate that all required data files exist
    2. Collect final metadata
    3. Run sanity checks and summarise results
    4. Back up data to research drive or cloud storage
    
    Args:
        folder_path: Path to experiment data folder.
    
    Example:
        ```python
        try:
            run_experiment()
        finally:
            wrapup(folder_path=experiment_folder)
        ```
    """
    console.rule("[bold cyan]Experiment Wrap-Up[/]")
    
    if not folder_path.exists():
        console.print(
            f"[Warning] Experiment folder not found: {folder_path}",
            style="yellow"
        )
        return
    
    required_files = ['copy_globals.py']
    validate_data_files(folder_path, required_files)
    
    collect_final_metadata(folder_path)
    
    run_sanity_checks(folder_path)
    
    backup_data(folder_path)
    
    console.rule("[bold green]Wrap-Up Complete[/]")
    console.print(
        f"✅ Experiment wrap-up completed for {folder_path.name}",
        style="green"
    )
