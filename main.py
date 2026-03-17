import hashlib

user_info = {
    
}

def hash_password(account_password):
    hashed_password = hashlib.sha256(account_password.encode()).hexdigest()
    return hashed_password

def sign_up(new_account_name,new_password,new_email):
    if new_account_name in user_info:
        return"Account name already exists"
    else:
        hashed_password = hash_password(new_password)
        user_info[new_account_name] = {
            "password": hashed_password,
            "email": new_email
        }
        return"Account created successfully"


def sign_in(account_name,account_password):
    if account_name in user_info:
        hashed_password = hash_password(account_password)
        if hashed_password == user_info[account_name]["password"]:
            return "Congratulations, account created successfully"

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
                user_info[account_name]["password"] = hashed_new_password
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
            return("Account deactivated")
        else:
            return("Incorrect password")
    
    else:
        return("Account does not exist")

# sign_up("Roland","12345","rolandtenkoko@gmail.com")
# print(user_info)
        