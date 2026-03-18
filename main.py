# Building a command line program that will be able to test my program and see if any errors areive


from user_info import sign_up
from user_info import sign_in
from user_info import forgot_password
from user_info import deactivate_account
from user_info import load_data
from user_info import save_data

load_data()
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
        print(result)

    elif request == 2:
        account_name = input("Enter your account name: ")
        account_password = input("Enter your password: ")
        result = sign_in(account_name, account_password)
        print(result)

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