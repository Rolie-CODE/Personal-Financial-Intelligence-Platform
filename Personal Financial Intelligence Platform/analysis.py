from storage import transaction_history


def get_financial_summary(user):

    income = 0
    expenses = 0

    transactions = transaction_history.get(user, [])


    for transaction in transactions:

        if transaction["type"] == "income":
            income += transaction["amount"]

        elif transaction["type"] == "expense":
            expenses += transaction["amount"]

    balance = income - expenses

    return {
        "Total Income": income,
        "Total Expenses": expenses,
        "Balance": balance
    }