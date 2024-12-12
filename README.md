
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
