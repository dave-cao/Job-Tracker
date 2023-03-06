import csv
from datetime import date

from flask import Flask, redirect, render_template, request, url_for

from handle_json import handle_json, save_jobs

app = Flask(__name__)


# Global Variables
jobs = []
job_length = 0


@app.context_processor
def get_year():
    return dict(year=date.today().year)


@app.route("/", methods=["GET", "POST"])
def home():
    global jobs
    global job_length

    if request.method == "POST":
        file = request.files["file"]

        jobs = handle_json(file)
        job_length = len(jobs)

        return render_template("index.html", jobs=jobs)

    return render_template("index.html", jobs=jobs)


@app.route("/job_page/<int:job_id>")
def job_page(job_id):

    selected_job = ""
    for job in jobs:
        if job["id"] == job_id:
            selected_job = job

    return render_template("job_page.html", job=selected_job)


@app.route("/status_change/<int:job_id>")
def change_status(job_id):
    global jobs

    progressions = {
        # contains a dictionary of tuples, (0, 1): 0 being status message
        # and 2 being the status colour
        "0": {"name": "status...", "color": "white", "progression": 0},
        "1": {"name": "Applied and Waiting", "color": "#FFFACD", "progression": 1},
        "2": {"name": "Interview Process", "color": "#FFA07A", "progression": 2},
        "3": {"name": "Offer", "color": "#98FB98", "progression": 3},
        "4": {"name": "Rejected", "color": "#FFB6C1", "progression": 4},
    }

    for job in jobs:
        if job["id"] == job_id:
            progression = job["status"]["progression"] + 1

            # reset progression back to default if out of range
            if progression >= len(progressions):
                progression = 0

            # increase progress by 1
            job["status"] = progressions[str(progression)]

    current_url = request.args.get("current_url", "Error occurred")
    if current_url == "home":
        return redirect(url_for("home"))
    else:
        return redirect(current_url)


@app.route("/<status>")
def tabbed(status):

    tabbed_jobs = [job for job in jobs if job["status"]["name"] == status]

    return render_template("tab.html", jobs=tabbed_jobs)


@app.route("/save")
def save():

    # Write job info into csv file
    save_jobs(jobs)

    current_url = request.args.get("current_url", "Error occurred")
    if current_url == "home":
        return redirect(url_for("home"))
    else:
        return redirect(current_url)


@app.route("/add", methods={"GET", "POST"})
def add():
    global jobs
    global job_length

    # Add a job posting to job tracker
    if request.method == "POST":
        job_length += 1

        # Put everything in a dictionary
        job_info = {
            "id": job_length,
            "title": request.form.get("jobtitle"),
            "company_name": request.form.get("company_name"),
            "application_link": request.form.get("application_link"),
            "application_details": request.form.get("application_details"),
            "job_description": request.form.get("job_description"),
            "status": {"name": "status...", "color": "white", "progression": 0},
        }

        jobs.insert(0, job_info)

        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/delete/<int:job_id>")
def delete(job_id):
    global jobs

    for job in jobs:
        if job["id"] == job_id:
            jobs.remove(job)

    current_url = request.args.get("current_url", "Error occurred")
    if current_url == "home":
        return redirect(url_for("home"))
    else:
        return redirect(current_url)


if __name__ == "__main__":
    app.run(debug=True)


# TODO Anki
