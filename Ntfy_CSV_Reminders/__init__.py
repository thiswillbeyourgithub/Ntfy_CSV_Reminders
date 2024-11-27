
import sys
import fire

from .Ntfy_CSV_Reminders import NtfyCSVReminders

__all__ = ["NtfyCSVReminders"]

__VERSION__ = NtfyCSVReminders.__VERSION__

def cli_launcher() -> None:
    if sys.argv[-1] ==  "--version":
        return(f"Ntfy_CSV_Reminders version: {__VERSION__}")
    fire.Fire(NtfyCSVReminders)

if __name__ == "__main__":
    cli_launcher()