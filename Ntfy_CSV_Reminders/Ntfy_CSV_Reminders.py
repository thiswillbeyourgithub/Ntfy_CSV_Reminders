from beartype import beartype
from pathlib import Path
import time
from typing import Union
# TODO_imports

@beartype  # this will apply to all methods
class NtfyCSVReminders:
    __VERSION__: str = "0.0.1"

    def __init__(
        self,
        input_csv: Union[str, Path],
        state_path: Union[str, Path],
        delay: int = 0
        ) -> None:

        """
        Initialize the NtfyCSVReminders class
        
        Args:
            input_csv: Path to input CSV file
            state_path: Path to state file
            delay: Number of seconds to delay/sleep after initialization
        """
        # Convert to Path objects if strings
        self.input_csv = Path(input_csv)
        self.state_path = Path(state_path)

        # Verify files exist
        assert self.input_csv.exists(), f"Input CSV file not found: {self.input_csv}"
        assert self.state_path.exists(), f"State file not found: {self.state_path}"
        if delay > 0:
            time.sleep(delay)

# TODO_code
