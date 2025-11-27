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
    - Implement retry logic for hardware checks that may fail intermittently

Structure:
    - setup(): Main setup function that orchestrates all checks
    - check_hardware_*(): Individual hardware validation functions
    - check_software_*(): Software and dependency checks
    - check_system_*(): System resource checks

Example Usage:
    ```python
    from .setup import setup
    
    hardware = setup()
    chiller = hardware['chiller']
    camera = hardware['camera']
    ```

Example Hardware Check:
    ```python
    def check_chiller(port: str) -> Optional[Chiller]:
        "Check chiller connection and functionality."
        try:
            chiller = Chiller(port)
            chiller.start()
            temp = chiller.get_temperature()
            console.print(f"Chiller connected. Current temperature: {temp}°C")
            return chiller
        except Exception as e:
            console.print(f"Chiller check failed: {e}")
            return None
    ```
"""

from typing import Dict, Optional, Any

from rich.console import Console
from rich.panel import Panel

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
    
    response = input("\nIs the hardware ready? (y/n): ")
    return response.lower() == 'y'


def setup() -> Optional[Dict[str, Any]]:
    """Run all pre-experiment setup checks and initialisation.
    
    This function orchestrates all setup tasks:
    1. System and dependency checks
    2. Hardware validation
    3. Disk space verification
    4. Initialising hardware objects
    
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
    input("\nPress Enter when ready to continue...")
    
    hardware_ready = check_hardware_example()
    if not hardware_ready:
        console.print(
            "[Error] Hardware check failed. Please verify connections.",
            style="red"
        )
        return None
    
    hardware = {}
    
    console.rule("[bold green]Setup Complete[/]")
    console.print("✅ All setup checks passed", style="green")
    
    return hardware if hardware else None
