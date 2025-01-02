def test_get_products_empty(client):
    response = client.get("/products/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_product(client):
    product_data = {
        "name": "Test Product",
        "description": "A test product",
        "price": 100.0,
        "stock": 10
    }
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 100.0
    assert data["stock"] == 10

def test_get_products_after_creation(client):
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Test Product"
