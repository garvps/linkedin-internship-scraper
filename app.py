from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, company, location, apply_link FROM internships")
    jobs = cursor.fetchall()
    conn.close()
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
