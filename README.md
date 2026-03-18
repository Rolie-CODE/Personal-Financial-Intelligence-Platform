💰 Personal Finance Intelligence Platform (PFIP)
Overview

The Personal Finance Intelligence Platform (PFIP) is a Python-based backend application designed to help users securely manage personal financial data. The system provides user account management and transaction tracking functionality, forming the foundation for future financial analytics and insights.

This project focuses on building strong backend fundamentals including data management, authentication logic, and persistent storage before adding optimization, security improvements, and analytics features.

✨ Features (Current)
👤 User Management

User registration (sign up)

Secure password hashing

User login (sign in)

Password reset functionality

Account deactivation

Password strength validation

💳 Transaction Management

Add transactions

View user transactions

Edit transactions

Delete transactions

Unique transaction IDs using UUID

Transactions linked to specific users

💾 Data Persistence

JSON-based storage

Automatic saving and loading of:

User data

Transaction history

🛠 Tech Stack

Python

JSON (data persistence)

hashlib (password hashing)

UUID (unique transaction IDs)

📁 Project Structure (Current)
PFIP/
│
├── users.py            # User authentication and account logic
├── transactions.py     # Transaction CRUD operations
├── storage.py          # Shared data structures
├── user_info.json      # Stored user data
├── transactions.json   # Stored transactions
└── README.md

🎯 Project Goals

This project is being developed incrementally with the following roadmap:

✅ User authentication system

✅ Transaction CRUD system

⏳ Financial analytics engine

⏳ API development with FastAPI

⏳ Dashboard visualization

⏳ Performance optimization

⏳ Security improvements

📚 Learning Objectives

This project is built to strengthen skills in:

Python backend development

Data modeling and storage

CRUD system design

Authentication logic

Software architecture fundamentals

🔮 Future Improvements

Monthly spending analytics

Category-based summaries

REST API endpoints

JWT authentication

Database migration (PostgreSQL/MySQL)

Interactive dashboard

📌 Status

🚧 Work in Progress — features are actively being added and improved.

👨‍💻 Author

Roland Tenkorang
