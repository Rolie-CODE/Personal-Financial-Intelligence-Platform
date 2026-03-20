import hashlib
import json
from storage import user_info


def save_data():
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file, indent=4)


def load_data():
    try:
        with open('user_info.json', 'r') as file:
            data = json.load(file)
            user_info.update(data)
    except FileNotFoundError:
        pass


def validate_password(new_password):

    if len(new_password) < 8:
        return "Password must be at least 8 characters long"

    if not any(char.isupper() for char in new_password):
        return "Password must contain an uppercase letter"

    if not any(char.islower() for char in new_password):
        return "Password must contain a lowercase letter"

    if not any(char.isdigit() for char in new_password):
        return "Password must contain a digit"

    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in new_password):
        return "Password must contain a special character"

    return None  


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def sign_up(name, password, email):

    if name in user_info:
        return "Account name already exists"

    error = validate_password(password)
    if error:
        return error

    user_info[name] = {
        "password": hash_password(password),
        "email": email
    }

    save_data()
    return "Account created successfully"


def sign_in(name, password):

    if name not in user_info:
        return "Account not found"

    if hash_password(password) == user_info[name]["password"]:
        return "Successful"

    return "Incorrect password"


def forgot_password(name, new_password, email):

    if name not in user_info:
        return "Account does not exist"

    if email != user_info[name]["email"]:
        return "Invalid email address"

    error = validate_password(new_password)
    if error:
        return error

    user_info[name]["password"] = hash_password(new_password)
    save_data()

    return "Password changed successfully"


def deactivate_account(name, password):

    if name not in user_info:
        return "Account does not exist"

    if hash_password(password) != user_info[name]["password"]:
        return "Incorrect password"

    del user_info[name]
    save_data()

    return "Account deactivated"