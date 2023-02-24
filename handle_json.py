import json


def handle_json(file):
    """File is a filestorage object from html input"""

    # file_data = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    data = json.loads(file.read().decode("UTF8"))
    return data


def save_jobs(jobs):

    json_object = json.dumps(jobs, indent=4)
    with open("jobs.json", "w") as file:
        file.write(json_object)

    return
