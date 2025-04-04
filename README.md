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
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download and set up the Firefox WebDriver (Geckodriver):
   - Download from: https://github.com/mozilla/geckodriver/releases
   - Add it to your system's PATH.

## Usage
### Running the Scraper
To start scraping LinkedIn job listings, run:
```bash
python scraper.py
```
This will generate a `linkedin_jobs.csv` file and populate `jobs.db` with scraped job postings.

### Running the Flask App
To start the web application and view job listings:
```bash
python app.py
```
Then, open a browser and visit `http://127.0.0.1:5000/`.

## Expected Output
- **CSV File (`linkedin_jobs.csv`)**:
  ```csv
  Title,Company,Location,Apply Link
  Software Engineer Intern, Google, California, https://linkedin.com/job-apply-link
  ```
- **Database (`jobs.db`)**: Stores job listings in a structured format.
- **Flask Web Interface**: Displays job listings in a simple table format.

## Troubleshooting
- **CAPTCHA Issues**: If LinkedIn prompts for CAPTCHA, try running the scraper with a logged-in session.
- **Blocked Requests**: Reduce request frequency or use proxy rotation.
- **WebDriver Not Found**: Ensure Geckodriver is installed and in PATH.

## Project Structure
```
linkedin-internship-scraper/
│-- scraper.py       # Web scraper using Selenium
│-- app.py           # Flask web application
│-- linkedin_jobs.csv # CSV file with scraped data
│-- jobs.db          # SQLite database
│-- requirements.txt # Python dependencies
│-- README.md        # Project documentation
│-- templates/       # Directory for HTML files
│   └── index.html   # Main HTML file for Flask app
```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

