user_info = {
    "account_name": {
        "password":"account_password",
        "email":"account_email"
    }
}

def sign_up(new_account_name,new_password,new_email):
    user_info[new_account_name] = {
        "password": new_password,
        "email": new_email
    }
    print("Account created successfully")


def sign_in(account_name,account_password):
    if account_name in user_info:
        if account_password == user_info[account_name]["password"]:
            print("Congratulations, you have logged in!")

    else:
        print("Account not found")

def forgot_password(account_name,new_account_password,account_email):
    if account_name in user_info:
        if account_email == user_info[account_name]["email"]:
            if new_account_password == user_info[account_name]["password"]:
                print("New password cannot be the same as old password")
            else:
                user_info[account_name]["password"] = new_account_password
                print("Password changed successfully")
        else:
            print("Invalid email address")  
    else:
        print("Account does not exist")

# sign_up("Rolandreads11","roro1234","rolandtenkoko@gmail.com")
# forgot_password("Rolandreads11","roro1234","rolandtenkoko@gmail.com")


        