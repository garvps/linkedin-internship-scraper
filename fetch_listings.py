from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup Firefox options
options = Options()
options.headless = True  # Set to True to run in headless mode
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# Start WebDriver
driver = webdriver.Firefox(options=options)

try:
    driver.get("https://www.linkedin.com/jobs/search/?keywords=Software%20Engineer%20Intern")

    # Wait for job cards to load
    wait = WebDriverWait(driver, 10)
    job_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'base-card')))

    jobs = []
    max_jobs = 40  # Adjust this to scrape more or fewer jobs


    def scroll_down():
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new jobs to load


    while len(jobs) < max_jobs:
        job_elements = driver.find_elements(By.CLASS_NAME, 'base-card')

        for job in job_elements:
            if len(jobs) >= max_jobs:
                break  # Stop when max_jobs limit is reached

            try:
                title = job.find_element(By.CLASS_NAME, "base-card__full-link").get_attribute("textContent").strip()
            except:
                title = "N/A"

            try:
                company = job.find_element(By.CLASS_NAME, "hidden-nested-link").get_attribute("textContent").strip()
            except:
                company = "N/A"

            try:
                location = job.find_element(By.CLASS_NAME, "job-search-card__location").get_attribute(
                    "textContent").strip()
            except:
                location = "N/A"

            try:
                apply_link = job.find_element(By.CLASS_NAME, "base-card__full-link").get_attribute("href")
            except:
                apply_link = "N/A"

            # Ensure job isn't duplicate
            if {"Title": title, "Company": company, "Location": location, "Apply Link": apply_link} not in jobs:
                jobs.append({"Title": title, "Company": company, "Location": location, "Apply Link": apply_link})

        scroll_down()  # Scroll to load more jobs

    # Save to CSV
    df = pd.DataFrame(jobs)
    df.to_csv("linkedin_jobs.csv", index=False)

    print("Scraping complete! Data saved to linkedin_jobs.csv")

finally:
    driver.quit()  # Ensures the driver quits even if an error occurs
