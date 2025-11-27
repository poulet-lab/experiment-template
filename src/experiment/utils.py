"""Utility functions for experiment management.

This module should contain common utility functions used throughout the experiment
for file operations, console output, path handling, and system information.

Best Practices:
    - Keep utility functions pure and reusable
    - Use type hints for all function parameters and return values
    - Provide clear docstrings explaining purpose and usage
    - Handle errors gracefully with informative messages
    - Use rich library for formatted console output

Common Utilities You Should Implement:
    - File and folder operations (create folders, save files, read files)
    - Path manipulation and validation
    - System information gathering (device name, username, disk space)
    - Data validation helpers
    - Date/time formatting

Example Functions Provided:
    - example_get_device_name(): Get hostname/device name
    - example_get_username(): Get current system username

Example Usage:
    ```python
    from rich.console import Console
    from .utils import example_get_device_name, example_get_username
    
    console = Console()
    console.rule("[bold cyan]Section Title[/]")
    console.print("Message", style="green")
    
    device = example_get_device_name()
    username = example_get_username()
    ```
"""

from rich.console import Console

console = Console()


def example_get_device_name() -> str:
    """Example: Get the hostname/device name of the current machine.
    
    This is an example function. Replace with your own implementation.
    
    Returns:
        Hostname string, or 'unknown' if unavailable.
    """
    import socket
    
    try:
        hostname = socket.gethostname() or socket.getfqdn()
        return hostname if hostname else "unknown"
    except Exception:
        return "unknown"


def example_get_username() -> str:
    """Example: Get the current system username.
    
    This is an example function. Replace with your own implementation.
    
    Returns:
        Username string, or 'unknown' if unavailable.
    """
    import getpass
    
    try:
        return getpass.getuser() or "unknown"
    except Exception:
        return "unknown"
