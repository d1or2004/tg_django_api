from fastapi import FastAPI
from product import product_router
from auth import auth_router

app = FastAPI()
app.include_router(product_router)
app.include_router(auth_router)


@app.get("/")
async def landing():
    return {
        "msg": "Landing Page"
    }
