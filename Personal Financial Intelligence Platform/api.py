# api.py
from fastapi import FastAPI
from user_info import sign_up, sign_in, forgot_password, deactivate_account, load_data, save_data
from transactions import add_transaction, view_transactions, delete_transaction, load_transactions, save_transactions
from analysis import *

# Load existing data
load_data()
load_transactions()

# Create FastAPI app
app = FastAPI(title="Royal Personal Finance API")

# Home End Point
@app.get("/")
def home():
    return {"result": "Royal Personal FInance Platform is running"}

# ------------------------
# User Endpoints
# ------------------------

@app.post("/signup")
def api_sign_up(account_name: str, password: str, email: str):
    """Create a new account"""
    result = sign_up(account_name, password, email)
    return {"result": result}

@app.post("/signin")
def api_sign_in(account_name: str, password: str):
    """Sign in with account credentials"""
    result = sign_in(account_name, password)
    return {"result": result}

@app.post("/forgot-password")
def api_forgot_password(account_name: str, new_password: str, email: str):
    """Reset password"""
    result = forgot_password(account_name, new_password, email)
    return {"result": result}

@app.post("/deactivate")
def api_deactivate_account(account_name: str, password: str):
    """Deactivate account"""
    result = deactivate_account(account_name, password)
    return {"result": result}

# ------------------------
# Transaction Endpoints
# ------------------------

@app.post("/transaction/add")
def api_add_transaction(user: str, amount: float, category: str, type: str, description: str, date: str):
    """Add a new transaction"""
    result = add_transaction(user, amount, category.lower().strip(), type.lower().strip(), description, date)
    return {"result": result}

@app.get("/transaction/view")
def api_view_transactions(user: str):
    """View all transactions for a user"""
    result = view_transactions(user)
    return {"transactions": result}

@app.delete("/transaction/delete")
def api_delete_transaction(user: str, transaction_id: str):
    """Delete a transaction by ID"""
    result = delete_transaction(user, transaction_id)
    return {"result": result}

@app.get("/transaction/summary")
def api_financial_summary(user: str):
    """Get user's financial summary (income - expenses)"""
    result = get_financial_summary(user)
    return {"balance": result}

@app.get("/spending/category/expense")
def api_spending_by_category(user:str):
    result = spending_by_category_expense(user)
    return {"summary": result}

@app.get("/spending/category/income")
def api_spending_by_category(user:str):
    result = spending_by_category_income(user)
    return {"summary": result}

@app.get("/monthly/summary")
def api_monthly_summary(user:str):
    result = monthly_summary(user)
    return result