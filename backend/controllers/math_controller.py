from fastapi import APIRouter, Depends, status

from schemas.factorial_schema import FactorialRequest, FactorialResponse
from schemas.fibonacci_schema import FibonacciRequest, FibonacciResponse
from services.factorial_service import FactorialService
from services.fibonacci_service import FibonacciService
from services.log_service import LogService
from utils.get_log_service import get_log_service

router = APIRouter(prefix="/math")


@router.post(
    "/factorial", response_model=FactorialResponse,
    status_code=status.HTTP_200_OK
)
def factorial(
    data: FactorialRequest,
    log_service: LogService = Depends(get_log_service)
):
    num = data.number
    result = FactorialService.get_factorial(num)
    log_service.log_request(
        "/math/factorial", "factorial", str(num),
        str(result), status.HTTP_200_OK
    )
    return {"result": result}


@router.post(
    "/fibonacci", response_model=FibonacciResponse,
    status_code=status.HTTP_200_OK
)
def fibonacci(
    data: FibonacciRequest,
    log_service: LogService = Depends(get_log_service)
):
    num = data.number
    sequence = FibonacciService.get_fibonacci(num)
    log_service.log_request(
        "/math/fibonacci", "fibonacci", str(num),
        str(sequence), status.HTTP_200_OK
    )
    return {"result": sequence}
