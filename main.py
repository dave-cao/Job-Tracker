from datetime import date

from flask import Flask, redirect, render_template, request, url_for

from handle_csv import handle_csv

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

    selected_job = None
    selected_i = None
    for i, job in enumerate(jobs):

        if job["id"] == str(job_id):
            status = job["status"][0]

            progressions = {
                "0": ("Applied and Waiting", "yellow"),
                "1": ("Interview Process", "orange"),
                "2": ("Offer", "green"),
                "3": ("Rejected", "red"),
            }

            print(status == "Rejected")
            if status == "status..." or status == "Rejected":
                job["status"] = progressions.get("0")
                job["progression"] = "0"
            elif job["status"] in progressions.values():
                progression = int(job["progression"]) + 1
                job["progression"] = str(progression)

                job["status"] = progressions.get(str(progression))

            # it's not a bug, it's a feature
            selected_job = job
            selected_i = i

    jobs = [selected_job] + jobs[:selected_i] + jobs[selected_i + 1 :]

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)


# TODO Anki
