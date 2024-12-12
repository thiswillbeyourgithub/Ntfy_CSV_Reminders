
# Ntfy_CSV_Reminders
Send a notification every few days as reminder. Inputs are based on a simple csv text file.

This tool was designed to be run daily via cron to send "unexpected" reminders at random intervals. Instead of getting the same reminder every X days, it uses probability to determine when to send notifications. This makes the reminders feel more spontaneous and can help prevent notification fatigue.

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
