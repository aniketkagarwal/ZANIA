from fastapi import FastAPI
from app.database import Base, engine
from app.routers import products, orders
from app.exceptions import custom_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ZANIA",
    description="A RESTful API for managing products and orders",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

# Custom exception handling
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return await custom_exception_handler(request, exc)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return await custom_exception_handler(request, exc)
