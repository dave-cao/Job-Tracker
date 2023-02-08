from datetime import date

from flask import Flask, render_template, request

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

    return render_template("index.html")


@app.route("/job_page/<int:job_id>")
def job_page(job_id):

    selected_job = ""
    for job in jobs:
        if job["id"] == str(job_id):
            selected_job = job

    return render_template("job_page.html", job=selected_job)


if __name__ == "__main__":
    app.run(debug=True)


# TODO Anki
