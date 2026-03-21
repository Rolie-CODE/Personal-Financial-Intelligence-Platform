# Royal Personal Finance Management System

## Overview

The **Royal Personal Finance Management System (RPFMS)** is a Python-based personal finance application that functions as both a **command-line application** and a **backend financial management system**. The platform allows users to manage accounts, record financial transactions, and generate analytical summaries through a structured backend architecture.

The project represents a transition from a learning application into a backend-oriented system designed with real software engineering principles, making it suitable for future API integration, database migration, and full-stack deployment.

---

## Project Objectives

* Build a structured backend system for personal financial management
* Implement secure user authentication workflows
* Provide transaction management through modular services
* Generate automated financial insights
* Develop backend-ready architecture suitable for API exposure
* Practice real-world software design and data handling

---

## System Role (Backend Perspective)

The application now operates as a **backend service layer**, responsible for:

* Managing user accounts and authentication logic
* Handling transaction data operations (CRUD)
* Performing financial analysis computations
* Persisting application data
* Serving as the core business logic that can power APIs or user interfaces

The CLI interface acts as a **client layer** interacting with backend modules.

---

## Features

### User Account Management

* User registration (Sign Up)
* Secure authentication (Sign In)
* Account deactivation
* Password recovery with verification
* Persistent user storage

### Transaction Management (Backend Logic)

* Add transactions
* View transaction history
* Edit transactions
* Delete transactions
* Categorization support
* Income and expense tracking
* Date-based transaction recording

### Financial Analysis Engine

* Financial summary generation
* Total income calculation
* Total expense calculation
* Balance computation

### Data Persistence

* Automatic loading of user and transaction data
* Automatic saving on application exit
* Separation of user and transaction storage logic

---

## Architecture

The system follows a modular backend architecture separating concerns across independent components.

```id="38j6ur"
Royal-Personal-Finance-System/
│
├── main.py              # Application entry point (CLI client)
├── user_info.py         # Authentication and user management service
├── transactions.py      # Transaction service (CRUD operations)
├── analysis.py          # Financial analysis service
├── data/                # Persistent storage files
└── README.md
```

### Architectural Design

* **Presentation Layer:** Command Line Interface
* **Service Layer:** Business logic modules
* **Data Layer:** Persistent storage handlers

This layered design allows easy migration to web or API environments.

---

## Backend Concepts Demonstrated

* Modular backend design
* Separation of concerns
* Service-oriented logic structure
* CRUD operation handling
* Authentication workflow implementation
* Data persistence management
* Financial computation services

---

## Recent Improvements

The project has evolved beyond a simple CLI application into a backend-capable system with the following updates:

* Conversion of core logic into reusable backend modules
* Dedicated transaction service architecture
* Integrated financial analysis engine (`get_financial_summary`)
* Improved navigation between authentication and transaction services
* Persistent save mechanisms for both users and transactions
* Structured transaction editing workflow
* Backend-ready function interfaces usable by APIs or external clients

---

## Future Development Roadmap

### Short-Term Enhancements

* Stronger input validation and error handling
* Transaction filtering by category and date range
* Pagination for transaction history
* Structured logging system

### Backend Expansion

* REST API implementation using FastAPI
* JWT authentication and authorization
* Database migration to PostgreSQL or MySQL
* ORM integration (SQLAlchemy)

### Analytics Improvements

* Monthly spending analytics
* Category-based financial insights
* Trend analysis and reporting

### Full-Stack Evolution

* Web dashboard frontend
* Visualization charts for financial data
* User profile management interface
* Cloud deployment with secure hosting

### Production-Level Goals

* API documentation (OpenAPI/Swagger)
* Role-based access control
* Automated testing suite
* Containerization using Docker

---

## Running the Project

### Requirements

* Python 3.x

### Setup

1. Clone the repository:

```id="sygxbx"
git clone https://github.com/your-username/royal-personal-finance-system.git
```

2. Navigate into the project folder:

```id="60fixi"
cd royal-personal-finance-system
```

3. Run the application:

```id="1o9n2f"
python main.py
```

---

## Example Workflow

1. Create an account
2. Authenticate into the system
3. Manage financial transactions
4. Generate financial summaries
5. Exit and automatically persist data

---

## Educational and Portfolio Value

This project demonstrates the progression from scripting to backend engineering by implementing real backend responsibilities such as authentication handling, data processing, and service-layer abstraction. It serves as a foundation for building scalable financial applications and API-driven platforms.

---

## Author

Developed as part of a backend development learning journey focused on software architecture, data systems, and financial application design.

---

## License

This project is intended for educational and portfolio use.
