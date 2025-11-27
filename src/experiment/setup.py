"""Pre-experiment initialisation and validation checks.

This module handles all pre-experiment setup tasks including hardware checks,
software validation, system resource verification, and experimenter reminders.

Best Practices:
    - Always run setup() at the beginning of every experiment
    - Check hardware connections and functionality before starting
    - Verify software dependencies and versions
    - Check disk space and system resources
    - Provide clear reminders and prompts for the experimenter
    - Return initialised hardware objects for use in the experiment
    - Implement retry logic using while loops - if a check fails or user says no,
      provide the opportunity to address the issue and try again
    - Use try/except blocks around hardware checks to handle errors gracefully
      and allow retries when hardware connections fail

Structure:
    - setup(): Main setup function that orchestrates all checks
    - check_hardware_*(): Individual hardware validation functions
    - check_software_*(): Software and dependency checks
    - check_system_*(): System resource checks

Below is an example of how to use the setup function to check the hardware.
"""

from typing import Dict, Optional, Any

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

from .globals import LOCAL_THRESHOLD_GB

console = Console()


def check_disk_space(path: str = ".") -> None:
    """Check available disk space before starting experiment.
    
    Args:
        path: Path to check disk space (default: current directory).
    """
    import shutil
    _, _, free = shutil.disk_usage(path)
    free_gb = free / (1024 ** 3)
    if free_gb < LOCAL_THRESHOLD_GB:
        console.print(
            f"[bold yellow]WARNING:[/bold yellow] "
            f"Only {free_gb:.2f} GB free. Please ensure sufficient space.",
            style="yellow"
        )


def check_hardware_example() -> bool:
    """Example hardware check function.
    
    This is a template for implementing hardware checks. Replace with
    actual hardware validation logic for your specific equipment.
    Use try/except blocks to handle connection errors gracefully.
    
    Returns:
        True if hardware check passes, False otherwise.
    """
    console.rule("[bold cyan]Hardware Check Example[/]")
    console.print(
        Panel(
            "This is an example hardware check.\n"
            "Replace this function with actual hardware validation.",
            border_style="yellow",
        )
    )
    
    try:
        response = Confirm.ask("\nIs the hardware ready?", default=True)
        return response
    except Exception as e:
        console.print(f"[Error] Hardware check failed: {e}", style="red")
        return False


def check_software_example() -> bool:
    """Example software check function.
    
    This is a template for implementing software checks. Replace with
    actual software validation logic for your specific software.
    Use try/except blocks to handle errors gracefully.
    
    Returns:
        True if software check passes, False otherwise.
    """
    console.rule("[bold cyan]Software Check Example[/]")
    console.print(
        Panel(
            "This is an example software check.\n"
            "Replace this function with actual software validation.",
            border_style="yellow",
        )
    )
    
    try:
        response = Confirm.ask("\nIs the software ready?", default=True)
        return response
    except Exception as e:
        console.print(f"[Error] Software check failed: {e}", style="red")
        return False


def check_system_example() -> bool:
    """Example system check function.
    
    This is a template for implementing system checks. Replace with
    actual system validation logic for your specific system.
    Use try/except blocks to handle errors gracefully.
    
    Returns:
        True if system check passes, False otherwise.
    """
    console.rule("[bold cyan]System Check Example[/]")
    console.print(
        Panel(
            "This is an example system check.\n"
            "Replace this function with actual system validation.",
            border_style="yellow",
        )
    )
    
    try:
        response = Confirm.ask("\nIs the system ready?", default=True)
        return response
    except Exception as e:
        console.print(f"[Error] System check failed: {e}", style="red")
        return False


def setup() -> Optional[Dict[str, Any]]:
    """Run all pre-experiment setup checks and initialisation.
    
    This function orchestrates all setup tasks:
    1. System and dependency checks
    2. Hardware validation
    3. Disk space verification
    4. Initialising hardware objects
    
    All checks are wrapped in while loops with try/except blocks to allow
    retries if checks fail or user indicates issues need to be addressed.
    
    Returns:
        Dictionary of initialised hardware objects, or None if setup fails.
    
    Example:
        ```python
        hardware = setup()
        if hardware:
            chiller = hardware.get('chiller')
            camera = hardware.get('camera')
        ```
    """
    console.rule("[bold cyan]Experiment Setup[/]")
    
    check_disk_space()
    
    console.print(
        Panel(
            "Please verify the following before continuing:\n"
            "1. All hardware is properly connected\n"
            "2. Software is running correctly\n"
            "3. Environment conditions are appropriate",
            border_style="cyan",
            title="Pre-Experiment Checklist"
        )
    )
    
    ready = Confirm.ask("\nAre you ready to continue?", default=True)
    if not ready:
        console.print("Setup cancelled by user.", style="yellow")
        return None
    
    while True:
        try:
            hardware_ready = check_hardware_example()
            if hardware_ready:
                break
            else:
                console.print(
                    "[Warning] Hardware check did not pass.",
                    style="yellow"
                )
                retry = Confirm.ask(
                    "Would you like to run the hardware check again?",
                    default=True
                )
                if not retry:
                    console.print(
                        "[Error] Hardware check failed. Please verify connections.",
                        style="red"
                    )
                    return None
        except Exception as e:
            console.print(
                f"[Error] Hardware check encountered an error: {e}",
                style="red"
            )
            retry = Confirm.ask(
                "Would you like to try the hardware check again?",
                default=True
            )
            if not retry:
                return None
    
    hardware = {}
    
    console.rule("[bold green]Setup Complete[/]")
    console.print("✅ All setup checks passed", style="green")
    
    return hardware if hardware else None
