from storage import transaction_history

def get_financial_summary(user):
    if user in transaction_history:
        for amount in transaction_history.values():
            if transaction_history["type"] == "income":
                income += amount
                return amount
            
