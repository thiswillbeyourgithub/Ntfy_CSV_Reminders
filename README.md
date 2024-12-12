
# Ntfy_CSV_Reminders
Simple phone notifications with random timing. Just write:
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
