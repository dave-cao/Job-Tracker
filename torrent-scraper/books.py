from pprint import pprint as pp

import requests
from bs4 import BeautifulSoup


class Books:
    def __init__(self):
        alt_site = ["https://audiobookbay.li"]

        # Website template and search term
        self.audiobook_url = "https://audiobookbay.se"
        self.book_list = []

    def get_audiobooks(self, query, page_number):
        """
        Grabs the audiobook title and urls from the specified search query
        """
        search_string = query.replace(" ", "+").lower()

        # seperate search query specifics with non-specifics
        targeted = []
        non_targeted = []

        # Get website data
        audiobook_search_url = (
            f"{self.audiobook_url}/page/{page_number}/?s={search_string}"
        )

        print("Getting response...")
        response = requests.get(audiobook_search_url, timeout=10)

        # extract all titles from page
        soup = BeautifulSoup(response.text, "lxml-xml")
        books = soup.find_all("div", class_="post")

        for book_id, book_post in enumerate(books):
            book_id += 1
            book = book_post.find("div", class_="postTitle")
            book_img = (
                book_post.find("div", class_="postContent").find("img").get("src")
            )
            print(book_img)

            # Increases book id number based on page number
            if page_number - 1:
                book_id = (book_id * (page_number - 1)) + 15

            title = book.get_text()
            link = book.find("a").get("href")
            link = f"{self.audiobook_url}{link}"

            if query.lower() in title.lower():
                targeted.append(Book(id=book_id, title=title, link=link, img=book_img))
            else:
                non_targeted.append(
                    Book(id=book_id, title=title, link=link, img=book_img)
                )

        book_list = targeted + non_targeted

        self.book_list = book_list
        return book_list, query  # returns a list of books

    def get_torrent_link(self, book_id):
        # book is a dictionary
        # grab the torrent link from selected website
        book_list = self.book_list
        book = [book for book in book_list if book.id == book_id][0]

        print("getting response again")
        response = requests.get(book.link, timeout=10)
        soup = BeautifulSoup(response.text, "lxml-xml")
        torrent_info = soup.find_all("tr")

        # grab the torrent link from the selected book
        for row in torrent_info:
            if "Torrent Download" in row.get_text():
                torrent_link = row.find("a").get("href")
                torrent_link = f"{self.audiobook_url}{torrent_link}"
                return torrent_link

        return "No link - ERROR"


class Book:
    def __init__(self, id, title, link, img):
        self.id = id
        self.title = title
        self.link = link
        self.img = img


# grab the torrent link from selected website
# selected_book = book_list["targeted"][0]
# selected_title, selected_link = selected_book
#
# # Get selected  book webpage
# response = requests.get(selected_link, timeout=10)
# soup = BeautifulSoup(response.text, "lxml-xml")
# torrent_info = soup.find_all("tr")
#
# # grab the torrent link from the selected book
# for row in torrent_info:
#     if "Torrent Download" in row.get_text():
#         torrent_link = row.find("a").get("href")
#         torrent_link = f"{audiobook_url}{torrent_link}"
#         print(torrent_link)
