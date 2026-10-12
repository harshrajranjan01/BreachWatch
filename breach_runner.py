
import os
from dotenv import load_dotenv

from database.account_manager import get_active_accounts
from breach_checker import check_breaches

load_dotenv()


def check_active_accounts():
    api_key = os.getenv("HIBP_API_KEY")

    if not api_key:
        print("Configuration Error: HIBP_API_KEY is missing.")
        return

    accounts = get_active_accounts()

    if accounts is None:
        print("Failed to retrieve monitored accounts.")
        return

    if not accounts:
        print("No active accounts found!")
        return

    print(f"Checking {len(accounts)} active account(s)...")
    print("=" * 35)

    for account in accounts:
        account_id, email = account

        print(f"Account ID: {account_id}")
        print(f"Email: {email}")

        try:
            breaches = check_breaches(email, api_key)

            if breaches is None:
                print("Status: API check failed.")

            elif breaches:
                print(f"Status: Found {len(breaches)} breach(es).")
                print("Breaches:")

                for breach in breaches:
                    print(f"- {breach.get('Name', 'Unknown breach')}")

            else:
                print("Status: No matching breaches found.")

        except Exception as error:
            print(f"Unexpected error while checking this account: {error}")

        print("-" * 35)


if __name__ == "__main__":
    check_active_accounts()
