import sqlite3

from fetch_listings import jobs

# Connect to database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create table
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

# Insert data
for job in jobs:
    cursor.execute("INSERT INTO internships (title, company, location, apply_link) VALUES (?, ?, ?, ?)",
                   (job["Title"], job["Company"], job["Location"], job["Apply Link"]))

conn.commit()
conn.close()
print("Data saved to database.")
