from storage import transaction_history

def get_financial_summary(user):
    if user in transaction_history:
        for amount in transaction_history.values():
            if transaction_history["type"] == "income":
                income += amount
                return income
            
        for amount in transaction_history.values():
            if transaction_history["type"] == "expenses":
                expenses += amount
                return expenses
            
    amount_left = income - expenses
    return amount_left
            
