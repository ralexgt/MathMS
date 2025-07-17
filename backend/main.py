from fastapi import FastAPI, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse

from services.log_service import LogService
from controllers.logs_controller import router as logs_router
from controllers.math_controller import router as math_router
from utils.get_log_service import get_log_service

app = FastAPI(
    title="Math Microservice",
    description="A microservice that does some computational work for you",
)

app.include_router(math_router)
app.include_router(logs_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Math microservice"}


@app.exception_handler(StarletteHTTPException)
async def handle_unreached_requests(
    request: Request, exc: StarletteHTTPException,
):
    # Only log 404s (you could log all if you want)
    if exc.status_code == 404:
        log_service: LogService = get_log_service()
        log_service.log_request(
            endpoint=request.url.path,
            operation=request.method,
            arguments="n/a",
            result="404 Not Found",
            status_code=404
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
