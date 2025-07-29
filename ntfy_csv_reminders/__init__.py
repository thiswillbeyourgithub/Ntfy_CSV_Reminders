import sys
import fire

from .ntfy_csv_reminders import NtfyCSVReminders

__all__ = ["NtfyCSVReminders"]

__VERSION__ = NtfyCSVReminders.__VERSION__


def cli_launcher() -> None:
    if "--version" in sys.argv:
        print(f"Ntfy_CSV_Reminders version: {__VERSION__}")
        return
    fire.Fire(NtfyCSVReminders)


if __name__ == "__main__":
    cli_launcher()
