import hashlib
import json
from transactions import load_transactions

from storage import user_info
from storage import transaction_history

def save_data():
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file, indent=4)

def load_data():
    global user_info
    try:
        with open('user_info.json', 'r') as file:
            data = json.load(file)
            user_info.update(data)
    except FileNotFoundError:
        return "No data file found. Starting with an empty user info." 
    
def validate_password(new_password):
    if len(new_password) < 8 :
        return "Password must be at least 8 characters long"


    elif not any(char.isupper() for char in new_password):
        return "Password must contain at least one uppercase letter"

    elif not any(char.islower() for char in new_password):
        return "Password must contain at least one lowercase letter"

    elif not any(char.isdigit() for char in new_password):
        return "Password must contain at least one digit"

    elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in new_password):
        return "Password must contain at least one special character"


def hash_password(account_password):
    hashed_password = hashlib.sha256(account_password.encode()).hexdigest()
    return hashed_password

def sign_up(new_account_name,new_password,new_email):
    if new_account_name in user_info:
        return"Account name already exists"
    else:
        validation_error = validate_password(new_password)
        if validation_error is not None:
            return validation_error
        hashed_password = hash_password(new_password)
        user_info[new_account_name] = {
            "password": hashed_password,
            "email": new_email
        }
        save_data()
        return "Account created successfully"



def sign_in(account_name,account_password):
    if account_name in user_info:
        hashed_password = hash_password(account_password)
        if hashed_password == user_info[account_name]["password"]:
            return "Successful"

        else:
           return "Incorrect password"

    else:
       return "Account not found!"

def forgot_password(account_name,new_account_password,account_email):
    if account_name in user_info:
        if account_email == user_info[account_name]["email"]:
            hashed_new_password = hash_password(new_account_password)
            if hashed_new_password == user_info[account_name]["password"]:
                return("New password cannot be the same as old password")
            else:
                validation_error = validate_password(new_account_password)  
                if validation_error is not None:
                    return validation_error
                user_info[account_name]["password"] = hashed_new_password
                save_data()
                return("Password changed successfully")
        else:
            return("Invalid email address")  
    else:
        return("Account does not exist")

def deactivate_account(account_name,account_password):
    if account_name in user_info:
        hashed_password = hash_password(account_password)
        if hashed_password == user_info[account_name]["password"]:
            del user_info[account_name]
            save_data()
            return("Account deactivated")
        else:
            return("Incorrect password")
    
    else:
        return("Account does not exist")
    

5