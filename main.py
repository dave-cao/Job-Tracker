import csv
from datetime import date

from flask import Flask, redirect, render_template, request, url_for

from handle_csv import handle_csv, save_jobs

app = Flask(__name__)


# Global Variables
jobs = []


@app.context_processor
def get_year():
    return dict(year=date.today().year)


@app.route("/", methods=["GET", "POST"])
def home():
    global jobs

    if request.method == "POST":
        file = request.files["file"]
        jobs = handle_csv(file)

        return render_template("index.html", jobs=jobs)

    return render_template("index.html", jobs=jobs)


@app.route("/job_page/<int:job_id>")
def job_page(job_id):

    selected_job = ""
    for job in jobs:
        if job["id"] == str(job_id):
            selected_job = job

    return render_template("job_page.html", job=selected_job)


@app.route("/status_change/<int:job_id>")
def change_status(job_id):
    global jobs

    for job in jobs:

        if job["id"] == str(job_id):
            status = job["status"][0]

            progressions = {
                # contains a dictionary of tuples, (0, 1): 0 being status message
                # and 2 being the status colour
                "0": ("Applied and Waiting", "yellow"),
                "1": ("Interview Process", "orange"),
                "2": ("Offer", "green"),
                "3": ("Rejected", "red"),
                "4": ("status...", "white"),
            }

            if status == "status...":
                job["status"] = progressions.get("0")
                job["progression"] = "0"
            elif job["status"] in progressions.values():
                progression = int(job["progression"]) + 1
                job["progression"] = str(progression)

                job["status"] = progressions.get(str(progression))

    current_url = request.args.get("current_url", "Error occurred")
    if current_url == "home":
        return redirect(url_for("home"))
    else:
        return redirect(current_url)


@app.route("/<status>")
def tabbed(status):

    tabbed_jobs = [job for job in jobs if job["status"][0] == status]

    return render_template("tab.html", jobs=tabbed_jobs)


@app.route("/save")
def save():

    # Write job info into csv file
    save_jobs(jobs)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)


# TODO Anki
