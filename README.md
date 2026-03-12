# E-commerce Back-end

This project implements an e-commerce system using FastAPI as the backend framework and MongoDB as the database.

Main features:

- User CRUD (account creation, update, and deletion)
- Product CRUD
- Shopping cart per user
- Payment simulation (order confirmation)

## Execution

### Python Virtual Environment

Creating, activating, and installing Python dependencies:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Database Creation

Creating a database using MongoDB:
```
mongosh create_database.js
```

### System Activation

Running from the project root:
```
uvicorn main:app --reload
```