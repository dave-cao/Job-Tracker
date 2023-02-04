import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# user search inputs
query = "python developer"
location = "Edmonton Alberta"

# make search inputs readable in url
query = query.replace(" ", "+")
location = location.replace(" ", "+")

params = {"q": query, "l": location}
headers = {
    "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate",
}

# Get info from website
job_sites = {
    "indeed": "https://ca.indeed.com/",
    "glassdoor": "https://www.glassdoor.ca/index.html",
    "monster": "https://www.monster.ca/",
    "linkedin": "https://www.linkedin.com/",
    "flexjobs": "https://www.flexjobs.com/",
    "ladders": "https://www.theladders.com/",
    "robert half": "https://www.roberthalf.ca/en/jobs",
}


# for job_site, url in job_sites.items():
#     response = requests.get(url)
#     print(response, job_site)
#
indeed_url = f"https://ca.indeed.com/jobs?q={query}&l={location}"
print(indeed_url)

# SELENIUM FOR THE BACK POCKET
driver = webdriver.Firefox()
driver.get(indeed_url)
page_source = driver.page_source

# soup = BeautifulSoup(page_source, "lxml-xml")
# print(soup.text)

time.sleep(5)
driver.close()


# TODO:
# Anki Cards
# 1. What is the params and header kwargs for in the requests module?
# 2. How to use selenium and beautiful soup together? --> selenium has .page_source
