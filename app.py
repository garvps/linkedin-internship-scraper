"""
Flask App: Internship Listings Viewer

This web application reads job listing data from a local SQLite database (jobs.db) and serves a webpage showing 
all the scrapped software engineering internship positions. The listings are fetched using a Selenium scraper and 
stored in the database before to running this app.
"""

# Import necessary libraries
from flask import Flask, render_template
import sqlite3

# Initializing the Flask application
app = Flask(__name__)

# Define the homepage route
@app.route("/")
def home():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, company, location, apply_link FROM internships")
    jobs = cursor.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    # Enable debug mode for hot reload and error messages
    app.run(debug=True)
