import sqlite3

conn = sqlite3.connect("cyber_incidents.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM vulnerability_details")
count = cursor.fetchone()[0]

print(f"Total records in DB: {count}")

cursor.execute("""
SELECT cvss, cwe_name, summary, source
FROM vulnerability_details
LIMIT 5
""")

rows = cursor.fetchall()

print("\nSample rows:")
for row in rows:
    print(row)

conn.close()
