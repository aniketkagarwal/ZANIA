from fastapi import HTTPException

def insufficient_stock_exception(product_id: int):
    raise HTTPException(status_code=400, detail=f"Insufficient stock for Product ID {product_id}.")

def product_not_found_exception(product_id: int):
    raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found.")
