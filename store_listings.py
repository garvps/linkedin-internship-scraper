"""
Store Scraped Job Listings into SQLite Database

This python script takes job listing data scraped from LinkedIn (in 'fetch_listings.py')
and saves it into an SQLite database. The database will store job title, company,
location, and apply link in the 'internships' table.
"""

#import necessary library
import sqlite3

#inport scraped jobs from 'fetch_listings.py'
from fetch_listings import jobs

#connect to the database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

#create the table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS internships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        company TEXT,
        location TEXT,
        apply_link TEXT
    )
    """
)

#inserting data
for job in jobs:
    cursor.execute("INSERT INTO internships (title, company, location, apply_link) VALUES (?, ?, ?, ?)",
                   (job["Title"], job["Company"], job["Location"], job["Apply Link"]))

conn.commit()
conn.close()
print("Data saved to database.")
