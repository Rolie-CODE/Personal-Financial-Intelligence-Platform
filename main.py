# Building a command line program that will be able to test my program and see if any errors areive


from user_info import sign_up
from user_info import sign_in
from user_info import forgot_password
from user_info import deactivate_account
from user_info import load_data
from user_info import save_data
from transactions import add_transaction
from transactions import load_transactions
from transactions import view_transactions
from transactions import edit_transaction
from transactions import delete_transaction
from transactions import save_transactions


def transaction_menu(account_name):
    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Edit Transaction")
        print("4. Delete Transaction")
        print("5. Exit")

        request = input("")
        try:
            request = int(request)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            return
        
        if request == 1:
            user = account_name
            amount = input("Enter the transaction amount: ")
            category = input("Enter the transaction category: ")
            type = input("Enter the transaction type (income/expense): ")
            description = input("Enter a description for the transaction: ")
            date = input("Enter the transaction date (YYYY-MM-DD): ")
            result = add_transaction(user,amount,category,type,description,date)
            print(result)

        elif request == 2:
            user = account_name
            result = view_transactions(user)
            print(result)
        
        elif request == 3:
            transaction_id = input("Enter the transaction ID: ")
            user = account_name
            amount = input("Enter the new transaction amount: ")
            category = input("Enter the new transaction category: ")
            type = input("Enter the new transaction type (income/expense): ")
            description = input("Enter a new description for the transaction: ")
            date = input("Enter the new transaction date (YYYY-MM-DD): ")
            result = edit_transaction(transaction_id, user, amount, category, type, description, date)
            print(result)

        elif request == 4:
            transaction_id = input("Enter the transaction ID: ")
            result = delete_transaction(transaction_id)
            print(result)

        elif request == 5:
            save_transactions()
            print("Exiting Transaction Management System. Goodbye!")
            return
        
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
            return
    
load_data()
load_transactions()
while True:
    print("Welcome to the Royal Personal Finance Management System!")
    print("-----------------------------------------------------------")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Forgot Password")
    print("4. Deactivate Account")
    print("5. Exit")

    request = input("")
    try:
        request = int(request)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    if request == 1:
        account_name = input("Enter your desired account name: ")
        account_password = input("Enter your desired password: ")
        account_email = input("Enter your email address: ")
        result = sign_up(account_name, account_password, account_email)
        print("Congratulations, you have successfully signed up!")

        if "successfully" in result:
            transaction_menu(account_name)

    elif request == 2:
        account_name = input("Enter your account name: ")
        account_password = input("Enter your password: ")
        result = sign_in(account_name, account_password)
        print(result)

        if "Successful" in result:
            transaction_menu(account_name)
        
    elif request == 3:
        account_email = input("Enter your email address: ")
        account_name = input("Enter your account name: ")
        account_password = input("Enter your new password: ")
        result = forgot_password(account_name,account_password,account_email)
        print(result)

    elif request == 4:
        account_name = input("Enter your account name: ")
        account_password = input("Enter your password: ")
        result = deactivate_account(account_name, account_password)
        print(result)

    elif request == 5:
        save_data()
        print("Thank you for using the Royal Personal Finance Management System!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")