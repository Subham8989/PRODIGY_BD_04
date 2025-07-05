# API Project with Flask, Flask-RESTful, and Redis Caching

## Overview
This project is a modular Flask API that uses Flask-RESTful for building RESTful endpoints and Redis caching (via Flask-Caching) to improve performance for frequently accessed data. The project follows a clean architecture with separate folders for models, routes, and database configuration.

---

## Features
- Flask-RESTful architecture
- SQLite database (`users.db`)
- Redis-based caching using Flask-Caching
- Modular structure
- Cache invalidation and expiration support

---

## Project Structure

```
api/
├── database/
│   └── users.db                  # SQLite database
├── models/
│   ├── __init__.py
│   └── UserModel.py             # SQLAlchemy User model
├── routes/
│   └── users/
│       ├── __init__.py
│       └── route.py             # User API endpoints
├── .flaskenv                    # Flask environment variables
├── .gitignore
├── .python-version
├── config.py                    # App configuration
├── extensions.py               # Extensions (e.g., cache, db)
├── pyproject.toml
├── README.md
├── run.py                       # Entry point
└── uv.lock
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Subham8989/PRODIGY_BD_04
cd PRODIGY_BD_04
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Redis Server
Make sure Redis is running locally on port `6379`. We can start it via Docker:
```bash
docker run -p 6379:6379 redis
```

Or via `redis-cli`
```bash
redis-cli
```

### 5. Run the Application
```bash
flask run
```

---

## Example API Endpoint

### Get All Users (with caching)
```
GET /users
```
Returns a list of users. Response is cached using Redis with a key prefix (e.g., `all_users`).

---

## Caching Details
- Uses **Flask-Caching** with Redis as the backend
- Common pattern: `@cache.cached(key_prefix='all_users')`
- Cache invalidation is done manually (e.g., after POST)
- Default timeout is set in `config.py`

---