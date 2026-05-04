from fastapi.testclient import TestClient
import pytest
import main

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def reset_database():
    main.products.clear()
    main.next_id = 1


def test_should_return_api_status_when_get_home():
    # Arrange

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Products API active!"}


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

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Mouse"
    assert data["price"] == 80.0
    assert data["in_stock"] is True


def test_should_list_products_when_products_exist():
    # Arrange
    client.post(
        "/products",
        json={
            "name": "Keyboard",
            "price": 150.0,
            "in_stock": True,
        },
    )

    # Act
    response = client.get("/products")

    # Assert
    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Keyboard"
    assert data[0]["price"] == 150.0


def test_should_get_product_by_id_when_product_exists():
    # Arrange
    client.post(
        "/products",
        json={
            "name": "Monitor",
            "price": 900.0,
            "in_stock": True,
        },
    )

    # Act
    response = client.get("/products/1")

    # Assert
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Monitor"
    assert data["price"] == 900.0
    assert data["in_stock"] is True


def test_should_return_not_found_when_product_does_not_exist():
    # Arrange

    # Act
    response = client.get("/products/999")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_should_return_validation_error_when_price_is_invalid():
    # Arrange
    payload = {
        "name": "Mouse",
        "price": -10.0,
        "in_stock": True,
    }

    # Act
    response = client.post("/products", json=payload)

    # Assert
    assert response.status_code == 422


def test_should_return_validation_error_when_name_is_invalid():
    # Arrange
    payload = {
        "name": "A",
        "price": 50.0,
        "in_stock": True,
    }

    # Act
    response = client.post("/products", json=payload)

    # Assert
    assert response.status_code == 422


def test_should_update_product_when_product_exists():
    # Arrange
    client.post(
        "/products",
        json={
            "name": "Mouse",
            "price": 80.0,
            "in_stock": True,
        },
    )

    payload = {
        "name": "Mouse Gamer",
        "price": 120.0,
        "in_stock": False,
    }

    # Act
    response = client.put("/products/1", json=payload)

    # Assert
    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Mouse Gamer"
    assert data["price"] == 120.0
    assert data["in_stock"] is False


def test_should_return_not_found_when_updating_product_that_does_not_exist():
    # Arrange
    payload = {
        "name": "Mouse Gamer",
        "price": 120.0,
        "in_stock": False,
    }

    # Act
    response = client.put("/products/999", json=payload)

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}


def test_should_delete_product_when_product_exists():
    # Arrange
    client.post(
        "/products",
        json={
            "name": "Mouse",
            "price": 80.0,
            "in_stock": True,
        },
    )

    # Act
    response = client.delete("/products/1")

    # Assert
    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product deleted sucessfully"
    assert data["product"]["id"] == 1
    assert data["product"]["name"] == "Mouse"


def test_should_return_not_found_when_deleting_product_that_does_not_exist():
    # Arrange

    # Act
    response = client.delete("/products/999")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found"}
