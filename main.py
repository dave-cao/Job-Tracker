import requests
from bs4 import BeautifulSoup

print("getting response")
response = requests.get("https://audiobookbay.se/", timeout=10)
print("got response")

soup = BeautifulSoup(response.text, "lxml-xml")

links = soup.find_all("a")
for link in links:
    href = link.get("href")

    if href:
        if "https" in href:
            print(href)
    # if href and href[:4] == "https":
    #    print(href)
