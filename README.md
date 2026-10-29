# Restful Booker API Test Automation Framework

A Python-based API test automation framework for testing the [Restful Booker API](https://restful-booker.herokuapp.com/).

The project demonstrates automated REST API testing using pytest, requests, JSON Schema validation, and the API Client pattern.

## Tech Stack

- **Python** — programming language
- **pytest** — test framework and fixtures
- **requests** — HTTP requests and session management
- **jsonschema** — API response schema validation
- **python-dotenv** — environment variable management
- **Git** — version control

## Project Structure

```text
api_restful_booker/
├── api/
│   ├── base_client.py
│   ├── booking_client.py
│   ├── auth_client.py
│   └── endpoints.py
├── data/
│   └── booking_data.py
├── schemas/
│   └── booking_schema.py
├── tests/
│   ├── test_create_booking.py
│   ├── test_delete_booking.py
│   ├── test_get_booking.py
│   ├── test_get_booking_ids.py
│   ├── test_ping.py
│   └── test_update_booking.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Test Coverage

The framework includes automated tests for:

- Retrieving booking IDs — `GET /booking`
- Retrieving a booking by ID — `GET /booking/{id}`
- Creating a booking — `POST /booking`
- Updating a booking — `PUT /booking/{id}`
- Deleting a booking — `DELETE /booking/{id}`
- Checking API health — `GET /ping`

Tests verify HTTP status codes, response data, and JSON Schema where applicable.

## Framework Architecture

The framework separates test logic from HTTP request handling.

- **BaseClient** provides reusable HTTP methods.
- **BookingClient** implements booking-related API operations.
- **AuthClient** handles authentication.
- **pytest fixtures** manage API clients, authentication tokens, and test data.
- **Fixture teardown** automatically cleans up created bookings.

## Installation

Clone the repository and navigate to the project directory.

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```dotenv
BASE_URL=https://restful-booker.herokuapp.com
API_USERNAME=your_username
API_PASSWORD=your_password
```

Replace the placeholder credentials with valid API credentials.

The `.env` file is excluded from Git to prevent accidental exposure of credentials.

## Running Tests

Run all tests:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_create_booking.py -v
```

## Key Concepts Demonstrated

- REST API testing and CRUD operations
- API Client pattern
- Object-oriented programming and inheritance
- pytest fixtures and fixture scopes
- Setup and teardown using `yield`
- HTTP session management
- Authentication using cookies
- JSON Schema validation
- Test data generation and cleanup

## Notes

The tests run against a public demo API. Results may occasionally be affected by service availability or changes made by other users.
