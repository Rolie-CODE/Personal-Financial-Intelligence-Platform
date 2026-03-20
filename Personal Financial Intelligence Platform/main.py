from user_info import *
from transactions import *
from analysis import get_financial_summary


def transaction_menu(account_name):

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Delete Transaction")
        print("4. Edit Transaction")
        print("5. Financial Summary")
        print("6. Exit")

        request = input("")

        try:
            request = int(request)
        except ValueError:
            print("Enter number between 1 and 6")
            continue

        if request == 1:

            amount = input("Amount: ")
            category = input("Category: ")
            type = input("Type (income/expense): ").lower().strip()
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")

            print(add_transaction(
                account_name, amount, category,
                type, description, date
            ))

        elif request == 2:
            print(view_transactions(account_name))

        elif request == 3:
            tid = input("Transaction ID: ")
            print(delete_transaction(account_name, tid))

        elif request == 4:
            tid = input("Transaction ID: ")
            amount = input("New amount: ")
            category = input("Category: ")
            type = input("Type: ")
            description = input("Description: ")
            date = input("Date: ")

            print(edit_transaction(
                account_name, tid,
                amount, category, type,
                description, date
            ))

        elif request == 5:
            print(get_financial_summary(account_name))

        elif request == 6:
            save_transactions()
            return


# ---------------- APP START ----------------

load_data()
load_transactions()

while True:

    print("Royal Personal Finance Management System")
    print("--------------------------------------------")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Deactivate Account")
    print("4. Forgot Password")
    print("5. Exit")

    choice = input("> ")

    if choice == "1":
        name = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        print(sign_up(name, password, email))

    elif choice == "2":
        name = input("Username: ")
        password = input("Password: ")

        if sign_in(name, password) == "Successful":
            transaction_menu(name)
        else:
            print("Login failed")

    elif choice == "3":
        name = input("Username: ")
        password= input("Password: ")
        print(deactivate_account(name,password))

    elif choice == "4":
        name = input("Account name: ")
        new_password = input("New Password: ")
        email = input("Email: ")
        print(forgot_password(name,new_password,email))

    elif choice == "5":
        save_data()
        break