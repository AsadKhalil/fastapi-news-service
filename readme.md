# FastAPI News Service

This is a FastAPI-based news service that periodically fetches news from an external API, stores it in a database (SQLite by default), and provides an API to retrieve the collected news. The service uses APScheduler for job scheduling and SQLAlchemy for database interactions. It is managed using **Poetry** for dependency management.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Migrations](#database-migrations)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)

## Features

- Fetches news periodically from a specified API endpoint using APScheduler.
- Stores fetched news items in an SQLite database (can be configured for other databases like PostgreSQL).
- Provides a FastAPI-based RESTful API to retrieve stored news with pagination support.
- Configurable via environment variables using Pydantic settings.

## Requirements

- Python 3.8+
- Poetry (for dependency management)
- FastAPI
- SQLAlchemy
- APScheduler
- Pydantic

## Project Structure

```
news_service/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── crud.py
│   ├── schemas.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── news_fetcher.py
│   ├── routers/
│       ├── __init__.py
│       ├── news.py
│
├── .env
├── pyproject.toml
└── README.md
```

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AsadKhalil/fastapi-news-service.git
   cd fastapi-news-service
   ```

2. **Install Dependencies with Poetry**

   Make sure you have Poetry installed. If not, you can install it using:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Now, install the dependencies:

   ```bash
   poetry install
   ```

3. **Activate the Virtual Environment**

   ```bash
   poetry shell
   ```

## Configuration

Copy the `.env.example` file to `.env` and adjust the settings as needed:

```
DATABASE_URL=sqlite:///./test.db
NEWS_FETCH_INTERVAL=15  # Interval in minutes to fetch news
NEWS_API_URL=https://news.10jqka.com.cn/tapp/news/push/stock/?page=1&tag=&track=website&pagesize={limit}
```

- `DATABASE_URL`: URL for the database connection (SQLite is the default).
- `NEWS_FETCH_INTERVAL`: The interval (in minutes) for the scheduler to fetch news.
- `NEWS_API_URL`: The URL endpoint to fetch news from.

## Running the Application

1. **Run the Application**

   ```bash
   poetry run uvicorn app.main:app --reload
   ```

   The service will be accessible at `http://127.0.0.1:8000`.

2. **Access API Documentation**

   FastAPI provides interactive API documentation at:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### GET `/news`

- **Description**: Retrieves the stored news items with pagination.
- **Parameters**:
  - `skip` (optional): The number of items to skip (for pagination).
  - `limit` (optional): The maximum number of items to return (default is 10).
- **Response**: JSON array of news items.

**Example Request**:

```bash
curl -X GET "http://127.0.0.1:8000/news?skip=0&limit=5" -H "accept: application/json"
```

## Logging

Logs are configured to output to the console. The logging level can be adjusted in the code, and logs include scheduler events, API requests, and errors.

## Troubleshooting

- **No Logs from the Scheduler**:
  - Ensure that the interval set in `.env` matches what is expected. Restart the server after changes.
  - Verify that the scheduler is starting by checking the logs during application startup.

- **Database Errors (e.g., column not found)**:
  - Make sure you’ve applied the latest migrations using Alembic or delete the SQLite database file to let it be recreated.

- **Scheduler Not Working as Expected**:
  - Confirm the APScheduler setup and that the job is added correctly in the `startup_event`.
  - Use `AsyncIOScheduler` with FastAPI for compatibility.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
