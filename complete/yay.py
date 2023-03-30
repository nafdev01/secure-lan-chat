import mariadb

# Set the database configuration parameters
config = {
    "user": "secure_admin",
    "password": "Annda8*j3s_Dje",
    "host": "10.1.133.254",
    "database": "secure_chat",
    "port": 3306,
}

# Connect to the remote database server
try:
    conn = mariadb.connect(**config)
except mariadb.Error as e:
    print(f"Error connecting to MariaDB: {e}")
    exit()

# Execute a query on the remote database
cursor = conn.cursor()
query = "SELECT * FROM users"
cursor.execute(query)

# Process the query results
for row in cursor:
    print(row)

# Close the database connection
cursor.close()
conn.close()
