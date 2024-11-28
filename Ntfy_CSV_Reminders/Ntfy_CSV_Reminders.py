import fire
import requests
from pathlib import Path
import json
import random
import time
from typing import Union, List, Tuple, Dict

class NtfyCSVReminders:
    __VERSION__: str = "0.0.1"

    def __init__(
        self,
        input_csv: Union[str, Path] = "inputs.csv",
        states_path: Union[str, Path] = "states.json",
        delay: int = 0,
        ntfy_topic: str = None,
        verbose: bool = False
        ) -> None:

        """
        Initialize the NtfyCSVReminders class

        Args:
            input_csv: Path to input CSV file
            states_path: Path to states file
            delay: Number of seconds to delay/sleep after initialization
            ntfy_topic: ntfy.sh topic
        """
        assert ntfy_topic.strip()
        self.ntfy_topic = ntfy_topic
        # Convert to Path objects if strings
        self.input_csv = Path(input_csv)
        self.states_path = Path(states_path)
        self.verbose = verbose

        # Verify files exist
        assert self.input_csv.exists(), f"Input CSV file not found: {self.input_csv}"
        if delay > 0:
            time.sleep(random.uniform(0, delay))

        # Load and validate CSV
        self.reminders: List[Tuple[int, str]] = []
        with open(self.input_csv, 'r') as f:
            content = f.read()
        rows = content.strip().splitlines()
        rows = [r.strip().split(",", 1) for r in rows if r.strip() and not r.startswith("#")]
        assert rows, "No rows found"
        for i, row in enumerate(rows):
            if len(row) != 2:
                raise ValueError(f"Row {i} must have exactly 2 elements, got {len(row)}")

            day_delay, text = row

            try:
                day_delay = int(day_delay)
            except ValueError:
                raise ValueError(f"Row {i}: First element must be a positive integer, got '{row[0]}'")
            if day_delay <= 0:
                raise ValueError

            # Validate second element is non-empty string
            text = text.strip()
            if not text:
                raise ValueError(f"Row {i}: Second element must be a non-empty string")

            self.reminders.append((day_delay, text))

        # Check for duplicate reminder texts
        reminder_texts = [reminder[1] for reminder in self.reminders]
        if len(reminder_texts) != len(set(reminder_texts)):
            duplicates = [text for text in reminder_texts if reminder_texts.count(text) > 1]
            raise ValueError(f"Duplicate reminder texts found: {', '.join(set(duplicates))}")

        # Load or create states file
        self.states: Dict[str, List[int]] = {}
        if self.states_path.exists():
            with open(self.states_path, 'r') as f:
                content = f.read().strip()
            if content:
                loaded = json.loads(content)
                assert isinstance(loaded, dict), type(loaded)
                for k, v in loaded.items():
                    self.states[k] = v
        else:
            # Create empty states file
            with open(self.states_path, 'w') as f:
                json.dump(self.states, f)

        for k, v in self.states.items():
            self.states[k] = sorted(v)

        try:
            self.loop()
        except Exception as e:
            self.__send_notif__(f"Error: '{e}'")


    def loop(self):
        """Check each reminder"""
        current_time = time.time()
        for day_delay, text in self.reminders:
            if text not in self.states:
                self.states[text] = []
                self.do_remind(day_delay, text)

            elif self.states[text]:  # If there are timestamps
                last_reminder = self.states[text][-1]
                days_since = (current_time - last_reminder) / (24 * 3600)
                chance = random.random()
                if days_since >= day_delay:
                    self.do_remind(day_delay, text)
                elif chance <= 1 / day_delay:
                    if self.verbose:
                        self.do_remind(day_delay, text + f"\nChance: {chance:.4f}\nThreshold: {1/day_delay:.4f}")
                    else:
                        self.do_remind(day_delay, text)


    def do_remind(self, day_delay: int, text: str):
        self.__send_notif__(message=text)
        self.states[text].append(int(time.time()))
        self.__save_states__()


    def __send_notif__(
        self,
        message: str,
        ):
        """
        Send a notification to a specified ntfy.sh topic.
        """
        requests.post(
            url=f"https://ntfy.sh/{self.ntfy_topic}" if "http" not in self.ntfy_topic else self.ntfy_topic,
            data=message.encode(encoding='utf-8'),
            headers={
                "Title": "Reminder",
                # "Priority": "urgent",
                # "Tags": "warning,skull"
            },
        )

    def __save_states__(self):
        with open(self.states_path, 'w') as f:
            f.write(json.dumps(self.states, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    fire.Fire(NtfyCSVReminders)
