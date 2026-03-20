from storage import transaction_history

def get_financial_summary(user):
    income = 0
    expenses = 0

    print(transaction_history)

    if user in transaction_history:
        for transaction in transaction_history[user]:

            if transaction["type"] == "income":
                income += transaction["amount"]

            elif transaction["type"] == "expenses":
                expenses += transaction["amount"]

    return income - expenses