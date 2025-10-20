import mysql.connector
from mysql.connector import Error

def connect_database():
        # Connect without specifying the database first
        connection = mysql.connector.connect(
            host="localhost",
            user="Zaina",
            password="Password123",
            auth_plugin='mysql_native_password'
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS booksdb;")
        print("✅ Database 'booksdb' verified or created.")

        # Now connect to it
        connection.database = "booksdb"
        print("✅ Connected to database:", connection.database)

if __name__ == "__main__":
    connect_database()

