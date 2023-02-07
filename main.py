from datetime import date

from flask import Flask, render_template, request

from handle_csv import handle_csv

app = Flask(__name__)


# Global Variables
@app.context_processor
def get_year():
    return dict(year=date.today().year)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        file = request.files["file"]
        file_data = handle_csv(file)

        return render_template("index.html", jobs=file_data)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# TODO Anki
# - How do you read a .csv file input without saving data and parsing it the csv library? - You want to make it an io object!
