import sqlite3
import pandas as pd

# Load the dataset
dataset_path = "All_Campus_Study_Spaces_With_Amenities.csv"
data = pd.read_csv(dataset_path)

# Connect to the SQLite database (or create it if it doesn't exist)
db_path = "study_spaces.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the `study_spaces` table
cursor.execute("""
CREATE TABLE IF NOT EXISTS study_spaces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    campus TEXT,
    building TEXT,
    room_name TEXT,
    popularity INTEGER,
    has_computers TEXT
);
""")
print("Table `study_spaces` created successfully (if not exists).")

# Insert data into the table
for _, row in data.iterrows():
    cursor.execute("""
    INSERT INTO study_spaces (campus, building, room_name, popularity, has_computers)
    VALUES (?, ?, ?, ?, ?);
    """, (row["campus"], row["building"], row["room_name"], row["popularity"], row["has_computers"]))

# Commit changes and close connection
conn.commit()
conn.close()

print(f"Data from {dataset_path} successfully added to {db_path}.")
