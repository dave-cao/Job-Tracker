from pprint import pprint as pp

import requests
from bs4 import BeautifulSoup

alt_site = ["https://audiobookbay.li"]

# Website template and search term
audiobook_url = "https://audiobookbay.se"
# audiobookbay_template = "https://audiobookbay.se/?s={}"
query = "Percy Jackson"
search_string = query.replace(" ", "+").lower()
audiobook_search_url = f"{audiobook_url}/?s={search_string}"


# Get website data
print("Getting response...")
response = requests.get(audiobook_search_url, timeout=10)

# extract all titles from page
soup = BeautifulSoup(response.text, "lxml-xml")
books = soup.find_all("div", class_="postTitle")

# seperate search query specifics with non-specifics
targeted = []
non_targeted = []
for book in books:
    title = book.get_text()
    link = book.find("a").get("href")
    link = f"{audiobook_url}{link}"

    if query in title:
        targeted.append([title, link])
    else:
        non_targeted.append([title, link])

book_list = {"targeted": targeted, "non_targeted": non_targeted}

# grab the torrent link from selected website
selected_book = book_list["targeted"][0]
selected_title, selected_link = selected_book

# Get selected  book webpage
response = requests.get(selected_link, timeout=10)
soup = BeautifulSoup(response.text, "lxml-xml")
torrent_info = soup.find_all("tr")

for row in torrent_info:
    if "Torrent Download" in row.get_text():
        torrent_link = row.find("a").get("href")
        torrent_link = f"{audiobook_url}{torrent_link}"
        print(torrent_link)

# extract torrent link from selected title

# Gets the links of each title
# for title in titles:
#     link = title.find("a")
#     href = link.get("href")
#     print(href)
#

# print("got response")

# soup = BeautifulSoup(response.text, "lxml-xml")
#
# links = soup.find_all("a")
# for link in links:
#     href = link.get("href")
#
#     if href:
#         if "https" in href:
#             print(href)
#     # if href and href[:4] == "https":
#     #    print(href)
