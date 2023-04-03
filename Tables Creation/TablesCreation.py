import mariadb
import sys

try:
    conn = mariadb.connect(
        user="atharva",
        password="my_password",
        host="127.0.0.1",
        port=3306,
        database="airportimmigrationmanagement"
    )
    conn.autocommit=False
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute("source tablesCreation.sql")

conn.commit()