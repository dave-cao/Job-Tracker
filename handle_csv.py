import csv
import io


def handle_csv(file):
    """File is a filestorage object from html input"""

    file_data = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    reader = csv.DictReader(file_data)

    jobs = [row for row in reader]

    # clean up details and description
    for i, job in enumerate(jobs):
        job["id"] = str(i)
        job["application_details"] = job["application_details"].strip("][")
        job["job_description"] = job["job_description"].strip("][").replace("\\n", "\n")

        # status
        job["status"] = ("status...", "white")
        job["progression"] = "0"

    return jobs
