from fastapi import FastAPI
from app.routes.product_routes import router

app = FastAPI()

app.include_router(router)