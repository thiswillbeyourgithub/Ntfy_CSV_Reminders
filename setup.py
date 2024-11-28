
from setuptools import setup, find_packages
from setuptools.command.install import install

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="Ntfy_CSV_Reminders",
    version="0.0.1",
    description="Probabilistic daily reminders via ntfy from csv",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiswillbeyourgithub/Ntfy_CSV_Reminders",
    packages=find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    keywords=["ntfy.sh", "reminders", "csv", "tool", "memory", "distraction", "distracted", "todo", "list"],
    python_requires=">=3.11",

    entry_points={
        'console_scripts': [
            'Ntfy_CSV_Reminders=Ntfy_CSV_Reminders.__init__:cli_launcher',
        ],
    },

    install_requires=[
        'fire >= 0.6.0',
    ]
)
