import json
import uuid
from storage import user_info, transaction_history


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


def add_transaction(user, amount, category, type, description, date):

    if user not in user_info:
        return "User does not exist"

    amount = float(amount)

    transaction_id = str(uuid.uuid4())

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

    amount = float(amount)

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