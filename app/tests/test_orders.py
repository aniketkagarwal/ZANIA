def test_create_order_insufficient_stock(client):
    product_data = {
        "name": "Product 1",
        "description": "A test product",
        "price": 50.0,
        "stock": 5
    }
    client.post("/products/", json=product_data)

    order_data = {
        "products": [{"id": 1, "quantity": 10}]
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient stock for Product ID 1."

def test_create_order_success(client):
    product_data = {
        "name": "Product 2",
        "description": "Another test product",
        "price": 20.0,
        "stock": 10
    }
    client.post("/products/", json=product_data)

    order_data = {
        "products": [{"id": 1, "quantity": 2}]
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["total_price"] == 40.0
    assert data["status"] == "completed"

def test_order_reduces_stock(client):
    response = client.get("/products/")
    data = response.json()
    assert data[0]["stock"] == 8
