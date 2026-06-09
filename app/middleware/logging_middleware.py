from fastapi import Request
import time


async def log_requests(request: Request, call_next):

    start_time = time.time()

    print(
        f"Request: {request.method} {request.url.path}"
    )

    response = await call_next(request)

    process_time = time.time() - start_time

    print(
        f"Response: {response.status_code} | "
        f"Time: {process_time:.4f}s"
    )

    return response

