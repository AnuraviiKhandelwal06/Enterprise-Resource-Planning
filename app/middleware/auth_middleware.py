from fastapi import Request
from fastapi.responses import JSONResponse

from app.utils.auth import verify_token


PUBLIC_ROUTES = [
    "/signup",
    "/login",
    "/docs",
    "/openapi.json",
    "/redoc"
]


async def authenticate_request(
    request: Request,
    call_next
):

    path = request.url.path

    print("Middleware hit:", path)

    # Allow public routes
    if path in PUBLIC_ROUTES:
        return await call_next(request)

    authorization = request.headers.get("Authorization")

    print("Authorization Header:", authorization)

    if not authorization:
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Authorization header missing"
            }
        )

    if not authorization.startswith("Bearer "):
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Invalid token format"
            }
        )

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_token(token)

    if not payload:
        return JSONResponse(
            status_code=401,
            content={
                "detail": "Invalid or expired token"
            }
        )

    request.state.user = payload

    return await call_next(request)