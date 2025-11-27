"""Experiment entry point and main execution flow.

This module serves as the main entry point for running experiments. It orchestrates
the complete experiment workflow: setup, execution, and wrapup.

Best Practices:
    - This should be the only script that users run directly (e.g., python -m src.experiment.run)
    - Use argparse for command-line argument parsing if needed
    - Implement signal handling for graceful shutdown (Ctrl+C)
    - Separate experiment logic into distinct functions that can be tested independently
    - Always call setup() before experiment execution
    - Always call wrapup() after experiment completion, even on errors (use try/finally)

Structure:
    - main(): Entry point that parses arguments and coordinates the workflow
    - experiment(): Core experiment logic (can be split into multiple functions)
    - signal_handler(): Handles interruption signals gracefully

Example Usage:
    ```bash
    python -m src.experiment.run
    ```

Example Workflow:
    ```python
    def main():
        folder_path = create_data_folder()
        hardware = setup(folder_path)
        
        try:
            experiment(folder_path, hardware)
        finally:
            wrapup(folder_path)
            cleanup(hardware)
    ```
"""

import signal
import sys
import time
from pathlib import Path
from typing import Optional

from rich.console import Console

from .globals import BASE_PATH
from .setup import setup
from .wrapup import wrapup

console = Console()


def copy_globals_to_experiment_folder(folder_path: Path) -> None:
    """Copy globals.py to experiment folder for parameter tracking.
    
    This ensures that the exact experimental parameters used in each session
    are preserved with the data, enabling full reproducibility.
    
    Args:
        folder_path: Path to the experiment data folder.
    """
    import shutil
    
    try:
        globals_source = Path(__file__).parent / "globals.py"
        globals_dest = folder_path / "copy_globals.py"
        
        if globals_source.exists():
            shutil.copy2(globals_source, globals_dest)
            console.print(
                f"✅ Saved experiment parameters to {globals_dest}",
                style="green"
            )
        else:
            console.print(
                "[Warning] globals.py not found, skipping copy",
                style="yellow"
            )
    except Exception as e:
        console.print(
            f"[Warning] Failed to copy globals.py: {e}",
            style="yellow"
        )


def signal_handler(sig: int, frame, hardware: Optional[object]) -> None:
    """Handle interruption signals gracefully.
    
    Args:
        sig: Signal number.
        frame: Current stack frame.
        hardware: Hardware object to clean up, if any.
    """
    console.print("\n[Signal] Ctrl+C detected. Forcing exit.")
    if hardware is not None:
        if hasattr(hardware, 'stop'):
            hardware.stop()
        if hasattr(hardware, 'close'):
            hardware.close()
    sys.exit(0)


def experiment(folder_path: Path, hardware: Optional[object]) -> None:
    """Execute the main experiment workflow.
    
    This function contains the core experiment logic. It should be organised
    into clear sections that can be easily understood and modified.
    
    Args:
        folder_path: Path to the experiment data folder.
        hardware: Initialised hardware objects from setup.
    
    Example:
        ```python
        def experiment(folder_path, hardware):
            collect_participant_info(folder_path)
            
            run_training_phase(folder_path, hardware)
            run_experimental_phase(folder_path, hardware)
            
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


def main() -> None:
    """Main entry point for the experiment.
    
    Sets up the experiment environment, runs the experiment, and handles cleanup.
    """
    import datetime
    current_date = datetime.datetime.now().strftime('%Y%m%d')
    folder_name = f"{current_date}_experiment"
    folder_path = BASE_PATH / "data" / "raw" / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    
    copy_globals_to_experiment_folder(folder_path)
    
    hardware = None
    try:
        hardware = setup()
        
        signal.signal(
            signal.SIGINT,
            lambda sig, frame: signal_handler(sig, frame, hardware)
        )
        
        experiment(folder_path, hardware)
        
    except KeyboardInterrupt:
        console.print("\n[Interrupt] Experiment interrupted by user", style="yellow")
    except Exception as e:
        console.print(f"\n[Error] Experiment failed: {e}", style="red")
        raise
    finally:
        if hardware is not None:
            if hasattr(hardware, 'stop'):
                hardware.stop()
            if hasattr(hardware, 'close'):
                hardware.close()
        
        wrapup(folder_path)


if __name__ == "__main__":
    main()

