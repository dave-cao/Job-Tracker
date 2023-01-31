from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from books import Books
from forms import QueryForm

# Initialize flask
app = Flask(__name__)
app.config["SECRET_KEY"] = "234kgja;dfj2p4gwejr;gv345pg;reoig"

# Initialize bootstrap
Bootstrap(app)

# initialize Book class
books = Books()
audiobooks = []


@app.route("/", methods=["GET", "POST"])
def home():
    form = QueryForm()
    if form.validate_on_submit():
        query = form.query.data
        book_list = books.get_audiobooks(query)
        return render_template("index.html", form=form, book_list=book_list)

    return render_template("index.html", form=form)


@app.route("/book_info/<int:book_id>")
def book_info(book_id):
    torrent_link = books.get_torrent_link(book_id)

    return render_template("book_info.html", torrent_link=torrent_link)


if __name__ == "__main__":
    app.run(debug=True)
