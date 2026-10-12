import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()


def get_db_connection():
    try:

        connection = mysql.connector.connect(host=os.getenv("DB_HOST"),
                                             user=os.getenv("DB_USER"),
                                             password=os.getenv(
            "DB_PASSWORD"),
            database=os.getenv("DB_NAME"),)

        if connection.is_connected():
            return connection

        else:
            connection.close()
            return None

    except mysql.connector.Error as error:
        print("MySQL connection failed.", error)
        return None
