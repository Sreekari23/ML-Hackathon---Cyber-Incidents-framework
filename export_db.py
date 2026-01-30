import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect("cyber_incidents.db")

# Read table into DataFrame
df = pd.read_sql_query(
    "SELECT * FROM vulnerability_details",
    conn
)

# Export to CSV
df.to_csv("cyber_incidents_export.csv", index=False)

conn.close()

print("✅ Database exported to cyber_incidents_export.csv")
