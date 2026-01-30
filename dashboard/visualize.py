import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("cyber_incidents.db")
cursor = conn.cursor()

cursor.execute("""
SELECT cwe_name, COUNT(*)
FROM vulnerability_details
GROUP BY cwe_name
""")

data = cursor.fetchall()
conn.close()

labels = [x[0] for x in data]
values = [x[1] for x in data]

plt.bar(labels, values)
plt.title("Vulnerabilities by CWE")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
