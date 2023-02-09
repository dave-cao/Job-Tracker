import requests


def save_file(url):

    url = "http://127.0.0.1:5000/"
    response = requests.get(url)

    print(response.text)


save_file("dummy")
