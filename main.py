import time
from pprint import pprint as pp

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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


indeed_url = f"https://ca.indeed.com/jobs?q={query}&l={location}"

# Initialize selenium
driver = webdriver.Firefox()

print("Opening web page...")
driver.get(indeed_url)
wait = WebDriverWait(driver, 10)


jobs = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".jcs-JobTitle"))
)
scraped_jobs = []
for job in jobs:

    # Scroll job into view and click
    driver.execute_script("arguments[0].scrollIntoView();", job)
    job.click()

    job_container = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".jobsearch-JobComponent"))
    )

    # Get the job title
    job_title = job_container.find_element(By.CSS_SELECTOR, "span")
    job_title = job_title.text[:-11]

    # Get the company name
    company_name = job_container.find_element(
        By.CSS_SELECTOR, ".jobsearch-InlineCompanyRating a"
    )
    company_name = company_name.text

    # Get the apply now link
    application_link = job.get_attribute("href")

    # Job Type - put it in a list
    job_type_container = job_container.find_elements(
        By.CSS_SELECTOR, "#jobDetailsSection div div"
    )
    key_words = ("Job type", "Application Details", "Salary")
    application_details = [
        job.text for job in job_type_container if job.text not in key_words
    ]

    # Job description
    job_description = job_container.find_element(By.CSS_SELECTOR, "#jobDescriptionText")
    job_description = job_description.text

    # Put everything in a dictionary
    job_info = {
        "title": job_title,
        "company_name": company_name,
        "application_link": application_link,
        "application_details": application_details,
        "job_description": job_description,
    }

    scraped_jobs.append(job_info)


# link = job_title.get_attribute("href")
pp(scraped_jobs)


driver.close()


# TODO:
# Anki Cards
# 1. What is the params and header kwargs for in the requests module?
# 2. How to use selenium and beautiful soup together? --> selenium has .page_source
# 3. How do you scroll into view an element with Selenium?
