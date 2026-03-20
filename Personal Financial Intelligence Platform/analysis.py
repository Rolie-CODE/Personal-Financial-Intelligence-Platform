from storage import transaction_history

def get_financial_summary(user):
    income = 0
    expenses = 0

    if user in transaction_history:

        for transaction in transaction_history[user]:

            if transaction["type"] == "income":
                income += transaction["amount"]

            elif transaction["type"] == "expenses":
                expenses += transaction["amount"]

    amount_left = income - expenses
    return amount_left
