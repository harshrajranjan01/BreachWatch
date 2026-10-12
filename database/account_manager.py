import mysql.connector
from database.connection import get_db_connection


def add_monitored_account():
    email = input("Enter Email Address: ")
    connection = None
    cursor = None

    try:
        connection = get_db_connection()

        if connection is None:
            print("Unable to connect to MySQL.")
            return False

        cursor = connection.cursor()

        query = "INSERT INTO monitored_accounts (email) VALUES(%s)"

        cursor.execute(query, (email,))

        connection.commit()
        print("Account added Successfully!!")
        return True

    except mysql.connector.IntegrityError:
        print("Error: This email already exists or violates a database constraint.")
        return False

    except mysql.connector.Error as error:
        print(f"Database error: {error}")
        return False

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def get_monitored_accounts():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()

        if connection is None:
            print("Unable to connect to MySQL.")
            return None

        cursor = connection.cursor()

        query = """
            SELECT id, email, is_active, created_at
            FROM monitored_accounts
        """

        cursor.execute(query)
        accounts = cursor.fetchall()

        return accounts

    except mysql.connector.Error:
        print("Database error: Unable to retrieve accounts.")
        return None

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


def listing_monitored_account():
    accounts = get_monitored_accounts()

    if accounts is None:
        print("Failed to retrieve accounts.")

    elif not accounts:
        print("No monitored accounts found.")

    else:
        print("Monitored accounts:")
        for account in accounts:
            account_id, email, is_active, created_at = account

            print(f"ID: {account_id}")
            print(f"Email: {email}")
            print(f"Active: {bool(is_active)}")
            print(f"Created at: {created_at}")
            print("-" * 25)


def set_monitoring_status():

    try:
        account_id = int(input('Enter Account Id: '))

    except ValueError:
        print("Please Enter Integers")
        return False

    if account_id:
        choice = input("Activate monitoring? (yes/no): ").strip().lower()
        if choice not in ("yes", "no"):
            print("Enter only yes or no")
            return False
        is_active = choice == "yes"

        connection = None
        cursor = None

        try:
            connection = get_db_connection()

            if connection is None:
                print("Unable to Connect to mysql")
                return None

            cursor = connection.cursor()
            query = "UPDATE monitored_accounts SET is_active = %s WHERE id = %s;"

            value = (is_active, account_id)

            cursor.execute(query, value)
            if cursor.rowcount == 0:
                print("No account was updated.")
                return False

            connection.commit()
            print("Account Updated Sucessfully!!")
            return True

        except mysql.connector.Error as error:
            print(f"MySQL Error: {error}")
            return False


def get_active_accounts():
    connection = None
    cursor = None
    try:
        connection = get_db_connection()

        if connection is None:
            print("Unable to connect to MYSQL")
            return None

        cursor = connection.cursor()

        query = "SELECT id, email FROM monitored_accounts WHERE is_active=%s"
        value = (True,)

        cursor.execute(query, value)

        active_accounts = cursor.fetchall()

        return active_accounts

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")
        return None

    finally:
        # Step 7: Close resources safely
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()
