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

def spending_by_category_expense(user):

    category_totals = {}

    if user not in transaction_history:
        return {}

    for transaction in transaction_history[user]:

        if transaction["type"] != "expense":
            continue

        category = transaction["category"]
        amount = float(transaction["amount"])

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals

def spending_by_category_income(user):

    category_totals = {}

    if user not in transaction_history:
        return {}

    for transaction in transaction_history[user]:

        if transaction["type"] != "income":
            continue

        category = transaction["category"]
        amount = float(transaction["amount"])

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    return category_totals