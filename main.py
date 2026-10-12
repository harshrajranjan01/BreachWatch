import os
from breach_checker import check_breaches
from database.account_manager import (
    add_monitored_account,
    get_monitored_accounts,
    listing_monitored_account,
    set_monitoring_status
)

print("=======================")
print("BreachWatch Started")
print("=======================")

while (True):
    print("1. Add Monitored Account")
    print("2. List Monitored Account")
    print("3. Enable/Disable Monitoring")
    print("4. Exit")

    try:
        option = int(input("Choose an option: "))

    except ValueError:
        print("\nPlease Enter A number!!")
        continue

    if option == 1:
        add_monitored_account()

    elif option == 2:
        listing_monitored_account()

    elif option == 3:
        set_monitoring_status()
        

    elif option == 4:
        break

    else:
        print("Enter Valid Choice")
