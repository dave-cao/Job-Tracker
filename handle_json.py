"""Handles utilizing the jobs.json file within the Job-Tracker application."""

import json


def handle_json(file):
    """Reads and decodes the file and returns the data in dictionary format.
    File is a filestorage object from html input."""
    data = json.loads(file.read().decode("UTF8"))
    return data


def save_jobs(jobs):
    """Saves the job dictionary into a json file."""
    json_object = json.dumps(jobs, indent=4)
    with open("jobs.json", "w") as file:
        file.write(json_object)
    return
