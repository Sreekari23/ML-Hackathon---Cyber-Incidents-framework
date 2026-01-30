import sqlite3

DB_NAME = "cyber_incidents.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS vulnerability_details")

    cursor.execute("""
    CREATE TABLE vulnerability_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cvss REAL,
        cwe_name TEXT,
        summary TEXT,
        source TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_vulnerability(cvss, cwe_name, summary, source):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO vulnerability_details (cvss, cwe_name, summary, source)
    VALUES (?, ?, ?, ?)
    """, (cvss, cwe_name, summary, source))

    conn.commit()
    conn.close()


# Run once to create table
if __name__ == "__main__":
    create_table()
