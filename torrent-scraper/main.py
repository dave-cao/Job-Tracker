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
    next_page = request.args.get("next_page")
    previous_page = request.args.get("previous_page")

    form = QueryForm()

    if form.validate_on_submit() or next_page or previous_page:
        # The query from form submit
        query = form.query.data

        # Get next or current page
        page_number = int(request.args.get("page", 0)) + 1

        # Get previous page
        if previous_page:
            page_number = int(request.args.get("page", 2)) - 1

            if page_number < 1:
                page_number = 1

        # If user clicks previous or next page, still grab query
        if not query:
            query = request.args.get("query")

        book_list = books.get_audiobooks(query, page_number=page_number)
        return render_template(
            "index.html", form=form, book_list=book_list, page_number=page_number
        )

    return render_template("index.html", form=form)


@app.route("/book_info/<int:book_id>")
def book_info(book_id):
    torrent_link = books.get_torrent_link(book_id)

    return render_template("book_info.html", torrent_link=torrent_link)


if __name__ == "__main__":
    app.run(debug=True)
