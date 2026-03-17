import json
import uuid
from storage import user_info
from storage import transaction_history

def save_transactions():
    with open('transactions.json', 'w') as file:
        json.dump(transaction_history, file, indent=4)

def load_transactions():
    global transaction_history
    try:
        with open('transactions.json', 'r') as file:
            data = json.load(file)
            transaction_history.update(data)
    except FileNotFoundError:
        transaction_history = {}

def add_transaction(user,amount,category,type,description,date):
    if user not in user_info():
        return "User does not exist"
    transaction_id = str(uuid.uuid4())
    transaction_history[transaction_id] = {
        "user": user,
        "amount": amount,
        "category": category,
        "type": type,
        "description": description,
        "date": date
    }
    save_transactions()
    return "Transaction added successfully"

def delete_transaction(transaction_id):
    if transaction_id in transaction_history:
        del transaction_history[transaction_id]
        save_transactions()
        return "Transaction deleted successfully"
    else:
        return "Transaction not found"

def view_transactions(user):
    if user not in user_info:
        return "User does not exist"
    user_transactions = {tid: details for tid, details in transaction_history.items() if details["user"] == user}
    return user_transactions

def edit_transaction(transaction_id, user, amount, category, type, description, date):
    if user not in user_info:
        return "User does not exist"
    if transaction_id in transaction_history:
        transaction_history[transaction_id] = {
            "user": user,
            "amount": amount,
            "category": category,
            "type": type,
            "description": description,
            "date": date
        }
        save_transactions()
        return "Transaction updated successfully"
    else:
        return "Transaction not found"