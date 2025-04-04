# LinkedIn Internship Scraper

This project is a Python-based web scraper that collects internship job listings from LinkedIn using the Selenium framework. The scraped data is saved to both a CSV file and an SQLite database. Additionally, a Flask web application is used to display the job listings from the database.

## Features
- Scrapes job listings from LinkedIn for "Software Engineer Intern" positions.
- Saves the scraped job data (title, company, location, apply link) to a CSV file (`linkedin_jobs.csv`).
- Saves the same job data to an SQLite database (`jobs.db`).
- A simple Flask web application displays the saved job listings on a webpage.

## Requirements
- Python 3.x
- Selenium
- Flask
- SQLite3 (comes with Python by default)
- Firefox WebDriver (Geckodriver)
- pandas

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/linkedin-internship-scraper.git
   cd linkedin-internship-scraper

