from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="ntfy-csv-reminders",
    version="0.1.11",
    description="Probabilistic daily reminders via ntfy from csv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiswillbeyourgithub/ntfy-csv-reminders",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    keywords=[
        "ntfy.sh",
        "reminders",
        "csv",
        "tool",
        "memory",
        "distraction",
        "distracted",
        "todo",
        "list",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "ntfy-csv-reminders=ntfy_csv_reminders.__init__:cli_launcher",
        ],
    },
    install_requires=[
        "fire >= 0.6.0",
        "requests >= 2.32.4",
        "caldav-tasks-api >= 1.4.0"
    ],
)
