
# 🛒 estore_api ![Python](https://img.shields.io/badge/python-3.11+-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.x-orange) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blueviolet) ![MongoDB](https://img.shields.io/badge/MongoDB-6.x-brightgreen)

## Overview

**estore_api** is a training project created as part of an intensive one-year Data Science course. Its primary goal is to build a backend API for an e-commerce store using modern technologies such as **FastAPI**, **SQLAlchemy**, **Docker**, and both **PostgreSQL** and **MongoDB** for data storage.

The project is developed to solidify backend development skills and to simulate real-world scenarios, following clean architecture and modular design patterns.

## Features

- 📦 **Product** and **Inventory** management
- 🗺️ **Locations** with capacity handling
- 📊 SQLite used for early development; PostgreSQL and MongoDB planned
- 🔌 Modular code structure following best practices
- 🧪 Ready for unit testing and API documentation via Swagger UI

## Technologies Used

- **Python 3.11+**
- **FastAPI** - lightweight API framework
- **SQLAlchemy** - ORM for SQL databases
- **SQLite / PostgreSQL** - relational database engines
- **MongoDB** - planned integration for document storage
- **Docker** - containerization for reproducible environments
- **uvicorn** - ASGI server
- **Pydantic** - data validation and serialization

## Project Structure

```

estore\_api/
├── app/
│   ├── core/             # Core configurations (e.g. settings, utils)
│   ├── crud/             # Create, Read, Update, Delete operations
│   ├── db/
│   │   ├── models/       # SQLAlchemy ORM models (Product, Location, Inventory)
│   │   ├── session.py    # SQLAlchemy engine and session config
│   ├── routers/          # FastAPI routers (to be implemented)
│   ├── schemas/          # Pydantic schemas (to be implemented)
│   └── management/       # Admin/utility tasks (to be implemented)
├── .venv/                # Virtual environment
├── README.md             # Project documentation
├── pyproject.toml        # Dependencies and build config
├── uv.lock               # Poetry lock file
└── .gitignore            # Git ignore rules

````

## Installation

```bash
# Clone the repository
git clone git@github.com:Kinetics20/estore_api.git
cd estore_api

# Sync dependencies (if you have 'uv' installed)
uv sync
````

## Usage

```bash
# Run the API using uvicorn
uvicorn app.main:app --reload
```

Visit the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs)

## Notes

* Current development uses **SQLite** (`inventory.db`) for rapid testing.
* PostgreSQL and MongoDB support will be added in upcoming phases.
* Docker integration planned for production environment and testing pipelines.

---

> This is a learning and training project for educational purposes.

## 💬 Feedback

Contributions and suggestions are welcome!

👤 **Author**: Piotr Lipiński
🗓 **Date**: June 2025
