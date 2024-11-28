from beartype import beartype
from pathlib import Path
import csv
import json
import random
import time
from typing import Union, List, Tuple, Dict
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
            time.sleep(random.uniform(0, delay))
            
        # Load and validate CSV
        self.reminders: List[Tuple[int, str]] = []
        with open(self.input_csv, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader, 1):
                # Validate row has exactly 2 elements
                if len(row) != 2:
                    raise ValueError(f"Row {i} must have exactly 2 elements, got {len(row)}")
                
                # Validate first element is positive int
                try:
                    day_delay = int(row[0])
                    if day_delay <= 0:
                        raise ValueError
                except ValueError:
                    raise ValueError(f"Row {i}: First element must be a positive integer, got '{row[0]}'")
                
                # Validate second element is non-empty string
                if not row[1].strip():
                    raise ValueError(f"Row {i}: Second element must be a non-empty string")
                
                self.reminders.append((day_delay, row[1].strip()))

        # Check for duplicate reminder texts
        reminder_texts = [reminder[1] for reminder in self.reminders]
        if len(reminder_texts) != len(set(reminder_texts)):
            duplicates = [text for text in reminder_texts if reminder_texts.count(text) > 1]
            raise ValueError(f"Duplicate reminder texts found: {', '.join(set(duplicates))}")

        # Load or create state file
        self.state: Dict[str, List[float]] = {}
        if self.state_path.exists():
            with open(self.state_path, 'r') as f:
                self.state = json.load(f)
        else:
            # Create empty state file
            with open(self.state_path, 'w') as f:
                json.dump(self.state, f)

# TODO_code
