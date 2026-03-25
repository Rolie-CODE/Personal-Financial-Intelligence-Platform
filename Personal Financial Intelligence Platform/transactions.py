import json
import uuid
from storage import user_info, transaction_history
from datetime import datetime

CATEGORIES = [
    "food",
    "transport",
    "housing",
    "bills",
    "shopping",
    "education",
    "entertainment",
    "health",
    "family",
    "income",
    "savings",
    "other"
]

allowed_type = ["income","expense"]

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transaction_history, file, indent=4)


def load_transactions():
    try:
        with open('transactions.json', 'r') as file:
            data = json.load(file)
            transaction_history.update(data)
    except FileNotFoundError:
        pass


from datetime import datetime, date

def validate_date(input_date):
    try:
        parsed_date = datetime.strptime(input_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    return parsed_date


def add_transaction(user, amount, category, type, description, date):

    if user not in user_info:
        return "User does not exist"

    try: 
        amount = float(amount)

    except ValueError:
        return "Amount should be a number"
    
    transaction_id = str(uuid.uuid4())

    validation_error = validate_date(date)
    if validation_error:
        return validation_error
    
    if category not in CATEGORIES:
        return "Invalid category"
    
    if type not in allowed_type:
        return "Type should only be income or expense"

    new_transaction = {
        "id": transaction_id,
        "amount": amount,
        "category": category,
        "type": type,
        "description": description,
        "date": date
    }


    if user not in transaction_history:
        transaction_history[user] = []

    transaction_history[user].append(new_transaction)

    save_transactions()
    return f"Transaction added successfully (ID: {transaction_id})"


def view_transactions(user):

    return transaction_history.get(user, [])


def delete_transaction(user, transaction_id):

    if user not in transaction_history:
        return "No transactions found"

    for transaction in transaction_history[user]:
        if transaction["id"] == transaction_id:
            transaction_history[user].remove(transaction)
            save_transactions()
            return "Transaction deleted successfully"

    return "Transaction not found"


def edit_transaction(user, transaction_id,
                     amount, category, type, description, date):

    if user not in transaction_history:
        return "No transactions found"

    try: 
        amount = float(amount)

    except ValueError:
        return "Amount should be a number"

    for transaction in transaction_history[user]:

        if transaction["id"] == transaction_id:
            transaction["amount"] = amount
            transaction["category"] = category
            transaction["type"] = type
            transaction["description"] = description
            transaction["date"] = date

            save_transactions()
            return "Transaction updated successfully"

    return "Transaction not found"