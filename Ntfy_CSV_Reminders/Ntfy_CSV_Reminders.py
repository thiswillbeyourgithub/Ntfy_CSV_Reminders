from beartype import beartype
import time
# TODO_imports

@beartype  # this will apply to all methods
class NtfyCSVReminders:
    __VERSION__: str = "0.0.1"

    def __init__(
        self,
        delay: int = 0
        ) -> None:

        """
        Initialize the NtfyCSVReminders class
        
        Args:
            delay: Number of seconds to delay/sleep after initialization
        """
        if delay > 0:
            time.sleep(delay)

# TODO_code
