import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Insert a new user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('ritika', '123'))

# Commit and close
conn.commit()
conn.close()