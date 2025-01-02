E-Commerce API
A production-grade RESTful API for managing products and orders in a simple e-commerce platform.

Features
* Product Management:
o View all products.
o Add new products with attributes like name, description, price, and stock quantity.
* Order Management:
o Place orders with validation for sufficient stock.
o Automatically deduct stock for successfully placed orders.
* Error Handling:
o Returns meaningful error responses for insufficient stock or invalid product IDs.
* Dockerized Deployment:
o Easily deployable using Docker.

Installation
* Prerequisites
o Python 3.9+
o Docker (for containerized deployment)
* Clone the Repository
o git clone <repository-url> 
o cd ZANIA
* Install Dependencies
o pip install -r requirements.txt
* Set Up the Database
o The database will automatically initialize when the application starts. By default, it uses SQLite.

Running the Application
* Local Development
o Start the FastAPI application:
* uvicorn app.main:app –reload
o Access the interactive API documentation at:
* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc
* Dockerized Deployment
o Build the Docker image:
* docker build -t ecommerce-api
o Run the container:
* docker run -p 8000:8000 ecommerce-api
o Access the API at http://127.0.0.1:8000/docs

API Endpoints
* Products
o GET /products
* Retrieves a list of all available products.
o POST /products
* Adds a new product.
* Example request body:

{
    "name": "Example Product",
    "description": "A sample product",
    "price": 49.99,
    "stock": 100
}

* Orders
o POST /orders
* Places an order.
* Example request body:

{
    "products": [
        {"id": 1, "quantity": 2},
        {"id": 2, "quantity": 1}
    ]
}

Testing
* Run Tests
o To execute the test suite, run:
* pytest app/tests/
* Test Coverage
o Unit Tests: Test individual endpoints and business logic.
o Integration Tests: Test interactions between endpoints and database.

