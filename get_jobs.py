import csv
import json
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
print(indeed_url)

# Initialize selenium
driver = webdriver.Firefox()

print("Opening web page...")
driver.get(indeed_url)
wait = WebDriverWait(driver, 10)


def get_page_info():
    """Returns all the jobs info in a dict of an Indeed page"""

    jobs = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".jcs-JobTitle"))
    )
    scraped_jobs = []

    # Scrape from page 1
    for job in jobs:

        # Make it so it's not like we're web scraping
        time.sleep(2)

        # Scroll job into view and click
        driver.execute_script("arguments[0].scrollIntoView();", job)
        job.click()

        job_container = wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".jobsearch-JobComponent")
            )
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
        job_description = job_container.find_element(
            By.CSS_SELECTOR, "#jobDescriptionText"
        )
        job_description = job_description.text

        # Put everything in a dictionary
        job_info = {
            "title": job_title,
            "company_name": company_name,
            "application_link": application_link,
            "application_details": application_details,
            "job_description": job_description,
            "status": {"name": "status...", "color": "white", "progression": 0},
        }

        scraped_jobs.append(job_info)

    return scraped_jobs


# Get info for all pages
pages = []
page_id = 0


while True:
    print("Getting current page info...")
    pages += get_page_info()

    # Next button
    try:
        # Click on next page button at end of page
        next_page_btn = driver.find_element(By.CSS_SELECTOR, "[aria-label='Next Page']")
        print("Getting next page...")
        next_page_btn.click()
    except NoSuchElementException:
        # if there is no more next pages, then end the loop
        print("End of page...")
        break

    # Linkedin Popup
    try:
        alert_obj_x = driver.find_element(
            By.CSS_SELECTOR, ".icl-CloseButton.icl-Modal-close"
        )
        print("Dam popups!")
        alert_obj_x.click()
    except NoSuchElementException:
        continue

# add a page id to each object
for page in pages:
    page["id"] = page_id
    page_id += 1

print("Creating json and inputting data...")
# Write job info into json file
# serializing json
json_object = json.dumps(pages, indent=4)

# writing to jobs.json
with open("jobs.json", "w") as file:
    file.write(json_object)


driver.close()


# TODO:
# Anki Cards
