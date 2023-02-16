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


def save_jobs(jobs):

    buffer = jobs.copy()
    with open("jobstemp.csv", "w", newline="") as file:
        fieldnames = [
            "id",
            "title",
            "company_name",
            "application_link",
            "application_details",
            "job_description",
            "status",
            "progression",
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for job in buffer:
            job["application_details"] = [job["application_details"]]
            job["job_description"] = [job["job_description"]]
            writer.writerow(job)

            job["application_details"] = job["application_details"][0]
            job["job_description"] = job["job_description"][0]
        return
