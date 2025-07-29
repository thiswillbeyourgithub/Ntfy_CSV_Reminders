
# ntfy_csv_reminders
A Python tool that sends random-timing phone notifications for recurring tasks by using daily probability checks based on CSV-defined frequencies.

Simple phone notifications with random timing. Just write a csv file like:
```
n, do something
```
And get reminded with 1/n probability each day. Perfect for those "should do this sometime this week" tasks!

Run it daily (via cron) and it uses probability to make reminders feel spontaneous rather than predictable. Great for avoiding notification fatigue while still keeping tasks on your radar.

# Getting started
* From pypi:
    * As a tool: `uvx ntfy_csv_reminders@latest --help`
    * Via uv: `uv pip install ntfy_csv_reminders`
    * Via pip: `pip install ntfy_csv_reminders`
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
ntfy_csv_reminders --ntfy_topic=your_topic [OPTIONS]
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
ntfy_csv_reminders --ntfy_topic=my_reminders --delay=1800 --input_csv=my_tasks.csv
```

# CalDAV Integration (Optional)
You can also automatically add your CSV reminders as tasks to a CalDAV-compatible task management system (like Nextcloud Tasks, Apple Reminders, etc.).

To enable CalDAV integration:
1. Install the optional dependency: `pip install caldav_tasks_api`
2. Set up environment variables for your CalDAV server:
   ```bash
   export CALDAV_TASKS_API_URL="https://your-server.com/remote.php/dav/"
   export CALDAV_TASKS_API_USERNAME="your_username"
   export CALDAV_TASKS_API_PASSWORD="your_password"
   export CALDAV_TASKS_API_LIST_UID="your_task_list_uid"  # Optional, uses first available if not set
   ```
3. Add the `--also_add_to_caldav` flag when running:
   ```bash
   ntfy_csv_reminders --ntfy_topic=my_reminders --also_add_to_caldav
   ```

Each CSV reminder will be created as a separate task in your CalDAV task list, with notes indicating the original frequency and source. This allows you to manage reminders both through notifications and your preferred task management app.

Note: Both this package and caldav_tasks_api are created by the same author for seamless integration.
