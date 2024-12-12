
# Ntfy_CSV_Reminders
A Python tool that sends random-timing phone notifications for recurring tasks by using daily probability checks based on CSV-defined frequencies.

Simple phone notifications with random timing. Just write a csv file like:
```
n, do something
```
And get reminded with 1/n probability each day. Perfect for those "should do this sometime this week" tasks!

Run it daily (via cron) and it uses probability to make reminders feel spontaneous rather than predictable. Great for avoiding notification fatigue while still keeping tasks on your radar.

# Getting started
* From pypi:
    * As a tool: `uvx Ntfy_CSV_Reminders@latest --help`
    * Via uv: `uv pip install Ntfy_CSV_Reminders`
    * Via pip: `pip install Ntfy_CSV_Reminders`
* From github:
    * Clone this repo then `pip install .`

# Example Input CSV
Create a file named `inputs.csv` with entries in this format:
```csv
5, Remember to water the plants
7, Time to clean the fish tank
3, Check the mail
```

Each line has two parts:
1. A number (X) representing "every X days" - this also determines the daily probability (1/X)
2. The reminder message

For example, with `5, Remember to water the plants`:
- If it's been 5+ days since the last reminder, it will definitely send
- Otherwise, each day there's a 1/5 (20%) chance to send the reminder

# Usage
```bash
Ntfy_CSV_Reminders --ntfy_topic=your_topic [OPTIONS]
```

Required:
- `--ntfy_topic`: Your ntfy.sh topic for receiving notifications
- `--input_csv`: Path to your CSV file (default: "inputs.csv")
- `--states_path`: Path to save reminder states (default: "states.json")

Optional:
- `--delay`: Random delay between 0-N seconds before checking reminders (default: 0)
- `--verbose`: Show probability details in notifications (default: False)

The `delay` parameter is particularly useful when running via cron. Instead of getting all reminders at exactly midnight (or whenever cron runs), adding something like `--delay=3600` will spread them randomly across the first hour. This makes the reminders feel even more natural and unexpected.

Example:
```bash
Ntfy_CSV_Reminders --ntfy_topic=my_reminders --delay=1800 --input_csv=my_tasks.csv
```
