<h1 align="center">Products API with FastAPI, Pydantic and Pytest</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white">
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white">
  <img src="https://img.shields.io/badge/Uvicorn-2A2A2A?style=for-the-badge&logo=python&logoColor=white">
</p>

<p align="center">
  REST API project for product management, built with FastAPI and tested with Pytest.
</p>

---

## Overview

This project was built to practice the fundamentals of backend API development with Python:

- creating HTTP routes with FastAPI;
- validating request data with Pydantic;
- returning structured JSON responses;
- handling errors with proper HTTP status codes;
- implementing CRUD operations;
- writing automated tests with Pytest;
- organizing tests using the Arrange, Act and Assert pattern.

The API manages a simple in-memory product list, making the project lightweight and focused on learning core REST concepts.

---

## Features

- Health check route for API status
- Product creation with validation
- Product listing
- Product search by ID
- Product update by ID
- Product deletion by ID
- Error handling for products that do not exist
- Validation errors for invalid product data
- Automated test suite with Pytest

---

## Tech Stack

- **Python**
- **FastAPI**
- **Pydantic**
- **Pytest**
- **Uvicorn**

---

## Data Model

Each product contains the following fields:

- `id`
- `name`
- `price`
- `in_stock`

---

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Returns API status |
| `GET` | `/products` | Lists all products |
| `GET` | `/products/{product_id}` | Gets a product by ID |
| `POST` | `/products` | Creates a new product |
| `PUT` | `/products/{product_id}` | Updates a product by ID |
| `DELETE` | `/products/{product_id}` | Deletes a product by ID |

---

## Request Example

```json
{
  "name": "Mouse",
  "price": 80.0,
  "in_stock": true
}
```

---

## Response Example

```json
{
  "id": 1,
  "name": "Mouse",
  "price": 80.0,
  "in_stock": true
}
```

---

## Validation Rules

- `name` must have at least 2 characters
- `price` must be greater than 0
- `in_stock` is optional and defaults to `true`

---

## Tests

The test suite covers:

- API status route
- product creation
- product listing
- product search by ID
- not found responses
- validation errors
- product update
- product deletion

Tests follow the Arrange, Act and Assert pattern:

```python
def test_should_create_product_when_payload_is_valid():
    # Arrange
    payload = {
        "name": "Mouse",
        "price": 80.0,
        "in_stock": True,
    }

    # Act
    response = client.post("/products", json=payload)

    # Assert
    assert response.status_code == 201
```

---

## How to Run

Install the dependencies:

```bash
pip install fastapi uvicorn pytest
```

Run the API:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

## How to Run Tests

```bash
python -m pytest -q
```

---

## Project Structure

```text
fastapi-produtos/
├── main.py
├── test_main.py
├── .vscode/
│   └── settings.json
└── README.md
```

---

## Learning Goals

This project is focused on practicing:

- REST API fundamentals
- HTTP methods and status codes
- request body validation
- response models
- exception handling
- automated backend testing
- clean and descriptive test naming
