from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from controllers.logs_controller import router as logs_router
from controllers.math_controller import router as math_router
from services.log_service import LogService
from utils.get_log_service import log_service_errors

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
    # Only log 404s for now
    result_ = {}
    if exc.status_code == 404:
        result_["detail"] = (
            "You are looking for something that I can not give you"
        )
        log_service: LogService = log_service_errors()
        log_service.log_request(
            endpoint=request.url.path,
            operation=request.method,
            arguments="n/a",
            result=result_["detail"],
            status_code=404
        )

    return JSONResponse(
        status_code=exc.status_code,
        content=result_
    )
