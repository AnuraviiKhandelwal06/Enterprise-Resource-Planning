from fastapi import FastAPI

from app.routes.product_routes import router
from app.routes.auth_routes import router as auth_router
from app.core.swagger_config import custom_openapi

from app.middleware.logging_middleware import log_requests
from app.middleware.auth_middleware import authenticate_request

app = FastAPI()

app.middleware("http")(log_requests)
app.middleware("http")(authenticate_request)

app.include_router(router)
app.include_router(auth_router)
def openapi():
    return custom_openapi(app)

app.openapi = openapi