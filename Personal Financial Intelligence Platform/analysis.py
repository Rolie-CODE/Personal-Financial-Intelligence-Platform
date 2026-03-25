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

def monthly_analysis(user,month):

    total_amount = 0
    if user not in transaction_history:
        return {}

    for transaction in transaction_history[user]:

        if month == "1":
            if not transaction["date"].startswith("2025-01"):
                month = "2025-01"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "2":
            if not transaction["date"].startswith("2025-02"):
                month = "2025-02"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "3":
            if not transaction["date"].startswith("2025-03"):
                month = "2025-03"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "4":
            if not transaction["date"].startswith("2025-04"):
                month = "2025-04"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "5":
            if not transaction["date"].startswith("2025-05"):
                month = "2025-05"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "6":
            if not transaction["date"].startswith("2025-06"):
                month = "2025-06"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "7":
            if not transaction["date"].startswith("2025-07"):
                month = "2025-07"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "8":
            if not transaction["date"].startswith("2025-08"):
                month = "2025-08"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "9":
            if not transaction["date"].startswith("2025-09"):
                month = "2025-09"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "10":
            if not transaction["date"].startswith("2025-10"):
                month = "2025-10"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "11":
            if not transaction["date"].startswith("2025-11"):
                month = "2025-11"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

        if month == "12":
            if not transaction["date"].startswith("2025-12"):
                month = "2025-12"
                continue

        amount = float(transaction["amount"])
        total_amount += amount

    return f"{month}: {total_amount}"

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